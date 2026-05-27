
from http.server import BaseHTTPRequestHandler
import base64
import json
import os
import re
from typing import Any, Dict, List, Optional

import cv2
import numpy as np


# -----------------------------
# Vercel Python ArUco endpoint
# -----------------------------

# Best default for real ArUco 4x4 markers.
# You can set this to "AUTO" if needed, but fixed is faster on Vercel.
DICTIONARY_NAME = os.environ.get("ARUCO_DICTIONARY", "DICT_4X4_50")

# Optional comma-separated allowed IDs, for example:
# Vercel Environment Variable: CUBE_FACE_IDS=0,1,2,3,4,5
CUBE_FACE_IDS_ENV = os.environ.get("CUBE_FACE_IDS", "").strip()

AUTO_DICT_ORDER = [
    "DICT_4X4_50", "DICT_4X4_100", "DICT_4X4_250", "DICT_4X4_1000",
    "DICT_5X5_50", "DICT_5X5_100", "DICT_5X5_250", "DICT_5X5_1000",
    "DICT_6X6_50", "DICT_6X6_100", "DICT_6X6_250", "DICT_6X6_1000",
    "DICT_7X7_50", "DICT_7X7_100", "DICT_7X7_250", "DICT_7X7_1000",
    "DICT_ARUCO_ORIGINAL",
]

_DETECTORS: Dict[str, Any] = {}


def parse_allowed_ids() -> Optional[List[int]]:
    if not CUBE_FACE_IDS_ENV:
        return None
    ids = []
    for part in CUBE_FACE_IDS_ENV.split(","):
        part = part.strip()
        if part:
            ids.append(int(part))
    return ids or None


CUBE_FACE_IDS = parse_allowed_ids()


def create_detector_parameters():
    if hasattr(cv2.aruco, "DetectorParameters"):
        params = cv2.aruco.DetectorParameters()
    else:
        params = cv2.aruco.DetectorParameters_create()

    tweaks = [
        ("adaptiveThreshWinSizeMin", 3),
        ("adaptiveThreshWinSizeMax", 45),
        ("adaptiveThreshWinSizeStep", 4),
        ("adaptiveThreshConstant", 7),
        ("minMarkerPerimeterRate", 0.02),
        ("maxMarkerPerimeterRate", 4.0),
        ("polygonalApproxAccuracyRate", 0.035),
        ("minCornerDistanceRate", 0.04),
        ("minDistanceToBorder", 2),
        ("cornerRefinementWinSize", 5),
        ("cornerRefinementMaxIterations", 40),
        ("cornerRefinementMinAccuracy", 0.03),
        ("errorCorrectionRate", 0.65),
    ]

    for attr, value in tweaks:
        if hasattr(params, attr):
            setattr(params, attr, value)

    if hasattr(params, "detectInvertedMarker"):
        params.detectInvertedMarker = True

    if hasattr(cv2.aruco, "CORNER_REFINE_SUBPIX") and hasattr(params, "cornerRefinementMethod"):
        params.cornerRefinementMethod = cv2.aruco.CORNER_REFINE_SUBPIX

    return params


class DetectorWrapper:
    def __init__(self, dictionary_name: str):
        self.dictionary_name = dictionary_name
        dict_id = getattr(cv2.aruco, dictionary_name)
        self.dictionary = cv2.aruco.getPredefinedDictionary(dict_id)
        self.params = create_detector_parameters()
        self.new_api = hasattr(cv2.aruco, "ArucoDetector")
        self.detector = cv2.aruco.ArucoDetector(self.dictionary, self.params) if self.new_api else None

    def detect(self, gray: np.ndarray):
        if self.new_api:
            corners, ids, _ = self.detector.detectMarkers(gray)
        else:
            corners, ids, _ = cv2.aruco.detectMarkers(gray, self.dictionary, parameters=self.params)
        return corners, ids


def get_detector(name: str) -> DetectorWrapper:
    if name not in _DETECTORS:
        _DETECTORS[name] = DetectorWrapper(name)
    return _DETECTORS[name]


def prepare_frames(frame: np.ndarray) -> List[np.ndarray]:
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    frames = [gray]

    # Keep contrast help, but not too many frames because Vercel has network/serverless overhead.
    clahe = cv2.createCLAHE(clipLimit=2.0, tileGridSize=(8, 8))
    frames.append(clahe.apply(gray))
    return frames


def decode_frame_from_json(payload: Dict[str, Any]) -> np.ndarray:
    data_url = payload.get("image", "")
    if not isinstance(data_url, str) or not data_url:
        raise ValueError("Missing image field")

    # Accept "data:image/jpeg;base64,...." or plain base64
    if "," in data_url:
        data_url = data_url.split(",", 1)[1]

    raw = base64.b64decode(data_url)
    arr = np.frombuffer(raw, dtype=np.uint8)
    frame = cv2.imdecode(arr, cv2.IMREAD_COLOR)

    if frame is None:
        raise ValueError("Could not decode image")

    return frame


def detect_markers(frame: np.ndarray) -> List[Dict[str, Any]]:
    names = AUTO_DICT_ORDER if DICTIONARY_NAME == "AUTO" else [DICTIONARY_NAME]
    allowed = set(CUBE_FACE_IDS) if CUBE_FACE_IDS is not None else None

    best_name = None
    best_corners = None
    best_ids = None
    best_count = 0

    for gray in prepare_frames(frame):
        for name in names:
            if not hasattr(cv2.aruco, name):
                continue

            detector = get_detector(name)
            corners, ids = detector.detect(gray)

            if ids is None or len(ids) == 0:
                continue

            ids_flat = ids.flatten().astype(int)

            if allowed is not None:
                keep = [i for i, marker_id in enumerate(ids_flat) if int(marker_id) in allowed]
                if not keep:
                    continue
                corners = [corners[i] for i in keep]
                ids_flat = np.array([ids_flat[i] for i in keep], dtype=int)

            count = len(ids_flat)
            if count > best_count:
                best_count = count
                best_name = name
                best_corners = corners
                best_ids = ids_flat

    if best_name is None or best_corners is None or best_ids is None:
        return []

    detections = []
    for corner_item, marker_id in zip(best_corners, best_ids):
        c = np.asarray(corner_item, dtype=np.float32).reshape(4, 2)
        detections.append({
            "dictionary": best_name,
            "id": int(marker_id),
            "corners": c.tolist(),
        })

    return detections


class handler(BaseHTTPRequestHandler):
    def _send_json(self, status: int, data: Dict[str, Any]) -> None:
        body = json.dumps(data).encode("utf-8")
        self.send_response(status)
        self.send_header("Content-Type", "application/json")
        self.send_header("Access-Control-Allow-Origin", "*")
        self.send_header("Access-Control-Allow-Methods", "POST, OPTIONS")
        self.send_header("Access-Control-Allow-Headers", "Content-Type")
        self.send_header("Cache-Control", "no-store")
        self.send_header("Content-Length", str(len(body)))
        self.end_headers()
        self.wfile.write(body)

    def do_OPTIONS(self):
        self._send_json(200, {"ok": True})

    def do_POST(self):
        try:
            length = int(self.headers.get("Content-Length", "0"))
            raw = self.rfile.read(length)
            payload = json.loads(raw.decode("utf-8"))

            frame = decode_frame_from_json(payload)
            detections = detect_markers(frame)
            h, w = frame.shape[:2]

            self._send_json(200, {
                "ok": True,
                "width": w,
                "height": h,
                "detections": detections,
                "dictionary": DICTIONARY_NAME,
            })
        except Exception as exc:
            self._send_json(500, {
                "ok": False,
                "error": str(exc),
            })
