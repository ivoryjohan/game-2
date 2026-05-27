<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8"/>
  <meta name="viewport" content="width=device-width, initial-scale=1.0, viewport-fit=cover"/>
  <title>Build Your Case - Vercel Python AR</title>
  <style>
    :root {
      --black:#000;
      --white:#fff;
      --paper:#e8e5e1;
      --lime:#98dc00;
      --muted:#777;
      --panel-w:390px;
      --safe-bottom: env(safe-area-inset-bottom, 0px);
    }

    * { box-sizing:border-box; }

    html, body {
      margin:0;
      width:100%;
      height:100%;
      overflow:hidden;
      background:var(--paper);
      font-family:Impact,"Arial Narrow","Roboto Condensed",Arial,sans-serif;
      user-select:none;
      -webkit-user-select:none;
      touch-action:none;
    }

    #app {
      width:100vw;
      height:100dvh;
      display:grid;
      grid-template-columns:minmax(0,1fr) var(--panel-w);
      background:var(--paper);
    }

    #cameraArea {
      height:100dvh;
      background:#050505;
      display:grid;
      place-items:center;
      overflow:hidden;
      position:relative;
    }

    #stage {
      position:relative;
      width:100%;
      height:100%;
      background:#000;
      overflow:hidden;
    }

    video, canvas {
      position:absolute;
      inset:0;
      width:100%;
      height:100%;
      display:block;
    }

    video { object-fit:fill; transform:translateZ(0); }
    #arCanvas { z-index:2; touch-action:none; cursor:crosshair; }

    #panel {
      height:100dvh;
      overflow:hidden;
      background:var(--paper);
      padding:16px 20px;
      border-left:2px solid var(--black);
      display:flex;
      flex-direction:column;
      gap:10px;
    }

    .header {
      height:86px;
      background:#000;
      color:#fff;
      padding:12px 14px;
      position:relative;
      flex:0 0 auto;
    }

    .mini { font-family:Arial,sans-serif; letter-spacing:.08em; color:#777; font-size:10px; line-height:1; }
    .code { position:absolute; right:14px; top:12px; }

    .title {
      font-size:32px;
      line-height:.86;
      letter-spacing:.02em;
      margin-top:14px;
      color:var(--white);
      text-transform:uppercase;
    }

    .plus { position:absolute; right:16px; bottom:14px; width:16px; height:16px; }
    .plus::before,.plus::after {
      content:""; position:absolute; background:var(--lime); left:50%; top:50%; transform:translate(-50%,-50%);
    }
    .plus::before { width:16px; height:2px; }
    .plus::after { width:2px; height:16px; }

    .status-card {
      border:1.5px solid #000;
      padding:8px 10px;
      min-height:58px;
      display:grid;
      grid-template-columns:46px 1fr 18px;
      gap:10px;
      align-items:center;
      flex:0 0 auto;
    }

    .status-card img { width:42px; height:42px; object-fit:contain; }

    .status-main { font-size:16px; line-height:1.05; text-transform:uppercase; }
    .status-sub {
      font-family:Arial,sans-serif;
      font-size:11px;
      letter-spacing:.04em;
      color:#666;
      margin-top:4px;
      white-space:nowrap;
      overflow:hidden;
      text-overflow:ellipsis;
    }

    .stripes { height:46px; background:repeating-linear-gradient(135deg,var(--lime) 0 4px,transparent 4px 10px); }

    .drag-banner {
      background:var(--lime);
      color:#000;
      border:2px solid #000;
      height:32px;
      display:flex;
      align-items:center;
      justify-content:space-between;
      padding:0 10px;
      text-transform:uppercase;
      flex:0 0 auto;
    }

    .drag-banner strong { font-size:18px; }
    .drag-banner span { font-family:Arial,sans-serif; font-size:11px; letter-spacing:.04em; }

    .section-head {
      display:flex;
      align-items:baseline;
      justify-content:space-between;
      flex:0 0 auto;
    }

    .section-head h3 { margin:0; font-size:18px; text-transform:uppercase; }
    .section-head span {
      font-family:Arial,sans-serif;
      color:#777;
      font-size:10px;
      letter-spacing:.08em;
      text-transform:uppercase;
    }

    #materials {
      display:grid;
      grid-template-columns:repeat(3,1fr);
      gap:8px;
      flex:0 0 auto;
    }

    .material {
      border:2px solid #000;
      height:52px;
      position:relative;
      overflow:hidden;
      background:#ddd;
      touch-action:none;
      cursor:grab;
    }

    .material.active { border-color:var(--lime); box-shadow:inset 0 0 0 2px var(--lime); }
    .material canvas { position:absolute; inset:0; width:100%; height:100%; }

    .material-label {
      position:absolute;
      left:0; right:0; bottom:0;
      height:16px;
      background:#000;
      color:#fff;
      font-size:10px;
      letter-spacing:.04em;
      line-height:16px;
      padding-left:5px;
      text-transform:uppercase;
      pointer-events:none;
    }

    .drag-dots {
      position:absolute;
      right:7px;
      top:7px;
      width:16px;
      height:16px;
      display:grid;
      grid-template-columns:repeat(2,1fr);
      gap:3px;
      pointer-events:none;
    }

    .drag-dots i {
      width:4px;
      height:4px;
      background:#000;
      border-radius:50%;
      display:block;
    }

    .row { display:grid; grid-template-columns:1fr 1fr; gap:10px; flex:0 0 auto; }
    .row.three { grid-template-columns:1fr 1fr 1fr; }

    button {
      border:2px solid #000;
      background:var(--paper);
      color:#000;
      height:36px;
      font-family:Impact,"Arial Narrow",Arial,sans-serif;
      font-size:14px;
      letter-spacing:.03em;
      text-transform:uppercase;
      touch-action:manipulation;
    }

    button.active { background:#000; color:#fff; border-color:var(--lime); }
    button:active { transform:scale(.985); background:var(--lime); color:#000; }

    .slider-card { border:1.5px solid #000; padding:8px 10px 10px; flex:0 0 auto; }
    .slider-top { display:flex; align-items:center; justify-content:space-between; margin-bottom:4px; }
    .slider-title { font-size:16px; text-transform:uppercase; }

    #brushPreview {
      width:34px;
      height:34px;
      border:2px solid #000;
      display:grid;
      place-items:center;
      background:#fff;
    }

    #brushDot { border-radius:50%; background:#38bdf8; border:1px solid #000; }

    input[type=range] { width:100%; accent-color:var(--lime); touch-action:pan-x; }

    #colors {
      display:grid;
      grid-template-columns:repeat(9,1fr);
      gap:6px;
      flex:0 0 auto;
    }

    .color { height:28px; border:2px solid #000; touch-action:manipulation; }
    .color.active { border-color:var(--lime); box-shadow:inset 0 0 0 2px var(--lime); }

    .bottom-card {
      border:1.5px solid #000;
      padding:10px 12px;
      font-family:Arial,sans-serif;
      font-size:12px;
      line-height:1.35;
      flex:1 1 auto;
      min-height:48px;
      overflow:hidden;
    }

    .bottom-card strong { color:var(--lime); }

    #ghost {
      position:fixed;
      width:92px;
      height:60px;
      pointer-events:none;
      z-index:10;
      border:2px solid var(--lime);
      display:none;
      opacity:.92;
      background:#ddd;
    }

    #message {
      position:fixed;
      left:16px;
      bottom:16px;
      background:rgba(0,0,0,.78);
      color:#fff;
      padding:10px 12px;
      font-family:Arial,sans-serif;
      font-size:13px;
      max-width:520px;
      z-index:20;
      display:none;
    }

    #startOverlay {
      position:fixed;
      inset:0;
      z-index:30;
      background:var(--paper);
      display:grid;
      place-items:center;
      padding:24px;
    }

    .start-box {
      width:min(590px,92vw);
      border:2px solid #000;
      background:var(--paper);
      padding:24px;
    }

    .start-box h1 { margin:0 0 12px; font-size:42px; line-height:.9; text-transform:uppercase; }
    .start-box p { font-family:Arial,sans-serif; line-height:1.45; color:#333; }

    .start-box button {
      width:100%;
      height:48px;
      margin-top:12px;
      background:#000;
      color:#fff;
    }

    .warning {
      border-left:6px solid var(--lime);
      padding-left:12px;
      font-family:Arial,sans-serif;
      font-size:13px;
      color:#333;
    }

    @media(max-width:980px),(orientation:portrait) {
      #app {
        grid-template-columns:1fr;
        grid-template-rows:1fr auto;
      }

      #cameraArea {
        height:calc(100dvh - 292px - var(--safe-bottom));
      }

      #panel {
        height:calc(292px + var(--safe-bottom));
        padding-bottom:calc(12px + var(--safe-bottom));
        border-left:0;
        border-top:2px solid #000;
        overflow-x:auto;
        overflow-y:hidden;
        display:grid;
        grid-template-columns:250px 230px 340px 230px 250px 230px 230px;
        gap:12px;
      }

      .header { height:100%; }
      .bottom-card { display:none; }
      #materials { grid-template-columns:repeat(3,96px); }
      .status-card { min-height:auto; }
    }
  </style>
</head>

<body>
  <div id="app">
    <main id="cameraArea">
      <div id="stage">
        <video id="video" autoplay muted playsinline></video>
        <canvas id="arCanvas"></canvas>
      </div>
    </main>

    <aside id="panel">
      <section class="header">
        <div class="mini">CONSTRAINT</div>
        <div class="mini code">PY</div>
        <div class="title">BUILD<br>YOUR CASE</div>
        <div class="plus"></div>
      </section>

      <section class="status-card">
        <img src="./assets/logo.png" alt="Build Your Case logo"/>
        <div>
          <div class="status-main" id="modeText">DRAW / FACE NONE</div>
          <div class="status-sub" id="selectedText">Selected: Grass</div>
        </div>
        <div class="stripes"></div>
      </section>

      <section>
        <div class="drag-banner">
          <strong>Drag & Drop</strong>
          <span>texture tiles to a face</span>
        </div>
        <div id="materials" style="margin-top:8px;"></div>
      </section>

      <section>
        <div class="row">
          <button id="applyBtn">Apply face</button>
          <button id="removeBtn">Remove</button>
        </div>
        <div class="row" style="margin-top:8px;">
          <button id="speedBtn">Speed</button>
          <button id="debugBtn">Debug</button>
        </div>
      </section>

      <section class="slider-card">
        <div class="slider-top">
          <div class="slider-title">Brush size <span id="brushSizeText">8</span></div>
          <div id="brushPreview"><div id="brushDot"></div></div>
        </div>
        <input id="brushSlider" type="range" min="2" max="52" value="8"/>
      </section>

      <section>
        <div class="section-head">
          <h3>Draw color</h3>
          <span>1-9</span>
        </div>
        <div id="colors"></div>
      </section>

      <section>
        <div class="row three">
          <button id="drawBtn" class="active">Draw</button>
          <button id="eraserBtn">Eraser</button>
          <button id="undoBtn">Undo</button>
        </div>
      </section>

      <section>
        <div class="row">
          <button id="clearFaceBtn">Clear face</button>
          <button id="clearAllBtn">Clear all</button>
        </div>
      </section>

      <section>
        <div class="row">
          <button id="fullscreenBtn">Fullscreen</button>
          <button id="switchCameraBtn">Switch cam</button>
        </div>
      </section>

      <section class="bottom-card">
        DRAG A MATERIAL TILE<br/>
        ONTO A CUBE FACE<br/>
        <strong>THEN DRAW OR ERASE.</strong>
      </section>
    </aside>
  </div>

  <div id="ghost"></div>
  <div id="message"></div>

  <div id="startOverlay">
    <div class="start-box">
      <h1>BUILD<br/>YOUR CASE</h1>
      <p>This Vercel version uses the camera of this phone/PC. The browser sends small frames to a Python/OpenCV ArUco detector on Vercel.</p>
      <p class="warning">Use HTTPS, allow camera access, use strong light, and keep the marker large in view. Python on Vercel will not be as fast as your local desktop app.</p>
      <button id="startBtn">Start camera</button>
    </div>
  </div>

  <canvas id="captureCanvas" style="display:none"></canvas>

  <script>
    "use strict";

    const video = document.getElementById("video");
    const canvas = document.getElementById("arCanvas");
    const ctx = canvas.getContext("2d");
    const stage = document.getElementById("stage");
    const captureCanvas = document.getElementById("captureCanvas");
    const captureCtx = captureCanvas.getContext("2d", { willReadFrequently: true });

    const ghost = document.getElementById("ghost");
    const messageBox = document.getElementById("message");
    const startOverlay = document.getElementById("startOverlay");
    const startBtn = document.getElementById("startBtn");

    const materialsEl = document.getElementById("materials");
    const colorsEl = document.getElementById("colors");
    const brushSlider = document.getElementById("brushSlider");
    const brushSizeText = document.getElementById("brushSizeText");
    const brushDot = document.getElementById("brushDot");
    const modeText = document.getElementById("modeText");
    const selectedText = document.getElementById("selectedText");

    const applyBtn = document.getElementById("applyBtn");
    const removeBtn = document.getElementById("removeBtn");
    const drawBtn = document.getElementById("drawBtn");
    const eraserBtn = document.getElementById("eraserBtn");
    const undoBtn = document.getElementById("undoBtn");
    const clearFaceBtn = document.getElementById("clearFaceBtn");
    const clearAllBtn = document.getElementById("clearAllBtn");
    const fullscreenBtn = document.getElementById("fullscreenBtn");
    const switchCameraBtn = document.getElementById("switchCameraBtn");
    const debugBtn = document.getElementById("debugBtn");
    const speedBtn = document.getElementById("speedBtn");

    const TRACK_PERSIST_FRAMES = 20;
    const PLANE_SCALE = 1.25;
    const TEXTURE_ALPHA = 0.92;
    const MAX_UV_JUMP = 0.24;
    const CONFIRM_FIRST_POINT_FRAMES = 2;
    const CONFIRM_FIRST_POINT_UV_RADIUS = 0.035;
    const CONFIRM_FIRST_POINT_SCREEN_RADIUS = 60;
    const DRAG_PREVIEW_SIZE = 68;

    const SPEED_MODES = [
      { name: "Quality", interval: 170, width: 760, jpeg: 0.70 },
      { name: "Balanced", interval: 130, width: 640, jpeg: 0.62 },
      { name: "Fast", interval: 95, width: 520, jpeg: 0.56 }
    ];
    let speedModeIndex = 1;

    const COLORS = [
      ["1", [56, 189, 248], "Blue"],
      ["2", [34, 197, 94], "Green"],
      ["3", [239, 68, 68], "Red"],
      ["4", [250, 204, 21], "Yellow"],
      ["5", [168, 85, 247], "Purple"],
      ["6", [255, 255, 255], "White"],
      ["7", [0, 0, 0], "Black"],
      ["8", [255, 140, 0], "Orange"],
      ["9", [255, 105, 180], "Pink"],
    ];

    let stream = null;
    let useFrontCamera = false;
    let detecting = false;
    let debugMode = false;
    let lastPointer = null;
    let detectionTimer = null;

    let tracks = new Map();
    let strokesByMarker = new Map();
    let texturesByMarker = new Map();
    let actionHistory = [];

    let activeKey = null;
    let currentStroke = null;
    let pendingFirstPoint = null;
    let pointerDown = false;
    let eraserMode = false;
    let eraserSnapshot = null;
    let eraserChanged = false;

    let brushColor = COLORS[0][1];
    let brushName = COLORS[0][2];
    let brushSize = 8;

    let currentTextureName = "Grass";
    let textures = new Map();
    let draggingTextureName = null;
    let brushPreviewUntil = 0;
    let lastDetectionInfo = "Python ready";

    startBtn.addEventListener("click", startCamera);
    applyBtn.addEventListener("click", () => activeKey ? applyTexture(activeKey, currentTextureName, true) : toast("Tap a cube face first."));
    removeBtn.addEventListener("click", () => activeKey ? removeTexture(activeKey, true) : toast("Tap a cube face first."));
    drawBtn.addEventListener("click", () => setEraser(false));
    eraserBtn.addEventListener("click", () => setEraser(true));
    undoBtn.addEventListener("click", undo);
    clearFaceBtn.addEventListener("click", () => activeKey ? clearFace(activeKey, true) : toast("Tap a cube face first."));
    clearAllBtn.addEventListener("click", () => clearAll(true));
    fullscreenBtn.addEventListener("click", toggleFullscreen);
    switchCameraBtn.addEventListener("click", switchCamera);
    debugBtn.addEventListener("click", () => {
      debugMode = !debugMode;
      debugBtn.classList.toggle("active", debugMode);
      toast(debugMode ? "Debug outlines on" : "Debug outlines off");
    });
    speedBtn.addEventListener("click", cycleSpeedMode);

    brushSlider.addEventListener("input", () => {
      brushSize = Number(brushSlider.value);
      updateBrushUI();
      showBrushPreview();
    });

    canvas.addEventListener("pointerdown", onPointerDown);
    canvas.addEventListener("pointermove", onPointerMove);
    canvas.addEventListener("pointerup", onPointerUp);
    canvas.addEventListener("pointercancel", onPointerUp);

    window.addEventListener("resize", resizeStage);
    window.addEventListener("keydown", handleKey);

    initTextures();
    initUI();
    updateBrushUI();
    updateModeUI();
    updateSpeedButton();

    async function startCamera() {
      try {
        if (!window.isSecureContext && location.hostname !== "localhost") {
          toast("Camera needs HTTPS. Deploy to Vercel or use localhost.");
          return;
        }

        if (stream) {
          stream.getTracks().forEach(track => track.stop());
          stream = null;
        }

        const constraints = {
          video: {
            facingMode: { ideal: useFrontCamera ? "user" : "environment" },
            width: { ideal: 1280 },
            height: { ideal: 720 },
            frameRate: { ideal: 30, max: 30 }
          },
          audio: false
        };

        stream = await navigator.mediaDevices.getUserMedia(constraints);
        video.srcObject = stream;
        await video.play();

        startOverlay.style.display = "none";
        resizeStage();

        if (detectionTimer) clearInterval(detectionTimer);
        detectionTimer = setInterval(detectFrame, SPEED_MODES[speedModeIndex].interval);

        requestAnimationFrame(render);
        toast("Camera started. Drag a texture tile onto a detected face.");
      } catch (error) {
        console.error(error);
        toast("Camera error: " + error.message);
      }
    }

    async function switchCamera() {
      useFrontCamera = !useFrontCamera;
      await startCamera();
    }

    function cycleSpeedMode() {
      speedModeIndex = (speedModeIndex + 1) % SPEED_MODES.length;
      if (detectionTimer) {
        clearInterval(detectionTimer);
        detectionTimer = setInterval(detectFrame, SPEED_MODES[speedModeIndex].interval);
      }
      updateSpeedButton();
      toast("Speed mode: " + SPEED_MODES[speedModeIndex].name);
    }

    function updateSpeedButton() {
      speedBtn.textContent = SPEED_MODES[speedModeIndex].name;
    }

    function resizeStage() {
      if (!video.videoWidth || !video.videoHeight) return;

      canvas.width = video.videoWidth;
      canvas.height = video.videoHeight;
      stage.style.aspectRatio = `${video.videoWidth} / ${video.videoHeight}`;

      const area = document.getElementById("cameraArea");
      const aw = area.clientWidth;
      const ah = area.clientHeight;
      const aspect = video.videoWidth / video.videoHeight;

      let w = aw;
      let h = w / aspect;
      if (h > ah) {
        h = ah;
        w = h * aspect;
      }

      stage.style.width = `${w}px`;
      stage.style.height = `${h}px`;
    }

    async function detectFrame() {
      if (detecting || !video.videoWidth) return;
      detecting = true;

      try {
        const mode = SPEED_MODES[speedModeIndex];
        const scale = Math.min(1, mode.width / video.videoWidth);
        captureCanvas.width = Math.round(video.videoWidth * scale);
        captureCanvas.height = Math.round(video.videoHeight * scale);
        captureCtx.drawImage(video, 0, 0, captureCanvas.width, captureCanvas.height);

        const dataUrl = captureCanvas.toDataURL("image/jpeg", mode.jpeg);
        const started = performance.now();

        const response = await fetch("/api/detect", {
          method: "POST",
          headers: { "Content-Type": "application/json" },
          body: JSON.stringify({ image: dataUrl })
        });

        const result = await response.json();
        if (!result.ok) throw new Error(result.error || "Detection failed");

        const sx = canvas.width / result.width;
        const sy = canvas.height / result.height;

        const detections = (result.detections || []).map(det => ({
          dictionary: det.dictionary,
          id: det.id,
          corners: det.corners.map(p => ({ x: p[0] * sx, y: p[1] * sy }))
        }));

        updateTracks(detections);
        lastDetectionInfo = `${detections.length} marker(s) | ${Math.round(performance.now() - started)}ms`;
      } catch (error) {
        console.warn(error);
        lastDetectionInfo = "Detection error";
      } finally {
        detecting = false;
        updateModeUI();
      }
    }

    function keyFor(dictionary, id) { return `${dictionary}:${id}`; }
    function idFromKey(key) { return Number(key.split(":")[1]); }

    function updateTracks(detections) {
      for (const track of tracks.values()) track.misses++;

      for (const det of detections) {
        const key = keyFor(det.dictionary, det.id);
        const corners = det.corners;

        if (tracks.has(key)) {
          const old = tracks.get(key);
          old.corners = stabilizeCorners(old.corners, corners);
          old.misses = 0;
          old.seen++;
        } else {
          tracks.set(key, { key, id: det.id, dictionary: det.dictionary, corners, misses: 0, seen: 1 });
        }
      }

      for (const [key, track] of tracks.entries()) {
        if (track.misses > TRACK_PERSIST_FRAMES) tracks.delete(key);
      }

      if ((!activeKey || !tracks.has(activeKey)) && visibleTracks().length) {
        activeKey = visibleTracks().sort((a, b) => polygonArea(b.corners) - polygonArea(a.corners))[0].key;
      }
    }

    function stabilizeCorners(oldCorners, newCorners) {
      const oldArea = Math.max(1, polygonArea(oldCorners));
      const newArea = Math.max(1, polygonArea(newCorners));
      const oldSize = Math.sqrt(oldArea);
      const oldCenter = polygonCenter(oldCorners);
      const newCenter = polygonCenter(newCorners);
      const centerJump = Math.hypot(newCenter.x - oldCenter.x, newCenter.y - oldCenter.y) / oldSize;
      const areaChange = Math.abs(newArea - oldArea) / oldArea;
      const still = centerJump < 0.03 && areaChange < 0.055;

      const centerAlpha = still ? 0.58 : 0.82;
      const shapeAlpha = still ? 0.22 : 0.62;
      const maxScaleStep = still ? 0.025 : 0.12;

      const smoothCenter = {
        x: centerAlpha * newCenter.x + (1 - centerAlpha) * oldCenter.x,
        y: centerAlpha * newCenter.y + (1 - centerAlpha) * oldCenter.y
      };

      const rawScale = Math.sqrt(newArea / oldArea);
      const limitedScale = Math.max(1 - maxScaleStep, Math.min(1 + maxScaleStep, rawScale));
      const scaleAdjust = rawScale > 1e-6 ? limitedScale / rawScale : 1;

      return newCorners.map((p, i) => {
        const oldShape = { x: oldCorners[i].x - oldCenter.x, y: oldCorners[i].y - oldCenter.y };
        const newShape = { x: (p.x - newCenter.x) * scaleAdjust, y: (p.y - newCenter.y) * scaleAdjust };
        return {
          x: smoothCenter.x + shapeAlpha * newShape.x + (1 - shapeAlpha) * oldShape.x,
          y: smoothCenter.y + shapeAlpha * newShape.y + (1 - shapeAlpha) * oldShape.y
        };
      });
    }

    function visibleTracks() { return Array.from(tracks.values()).filter(t => t.misses <= TRACK_PERSIST_FRAMES); }

    function polygonCenter(points) {
      let x = 0, y = 0;
      for (const p of points) { x += p.x; y += p.y; }
      return { x: x / points.length, y: y / points.length };
    }

    function polygonArea(points) {
      let area = 0;
      for (let i = 0; i < points.length; i++) {
        const j = (i + 1) % points.length;
        area += points[i].x * points[j].y - points[j].x * points[i].y;
      }
      return Math.abs(area) / 2;
    }

    function getStrokes(key) {
      if (!strokesByMarker.has(key)) strokesByMarker.set(key, []);
      return strokesByMarker.get(key);
    }

    function makeProjector(corners) {
      const p0 = corners[0], p1 = corners[1], p2 = corners[2], p3 = corners[3];
      const x0 = p0.x, y0 = p0.y, x1 = p1.x, y1 = p1.y, x2 = p2.x, y2 = p2.y, x3 = p3.x, y3 = p3.y;
      const dx1 = x1 - x2, dy1 = y1 - y2, dx2 = x3 - x2, dy2 = y3 - y2, dx3 = x0 - x1 + x2 - x3, dy3 = y0 - y1 + y2 - y3;
      let a, b, c, d, e, f, g, h;

      if (Math.abs(dx3) < 1e-6 && Math.abs(dy3) < 1e-6) {
        a = x1 - x0; b = x3 - x0; c = x0; d = y1 - y0; e = y3 - y0; f = y0; g = 0; h = 0;
      } else {
        const denominator = dx1 * dy2 - dx2 * dy1;
        if (Math.abs(denominator) < 1e-6) return null;
        g = (dx3 * dy2 - dx2 * dy3) / denominator;
        h = (dx1 * dy3 - dx3 * dy1) / denominator;
        a = x1 - x0 + g * x1; b = x3 - x0 + h * x3; c = x0;
        d = y1 - y0 + g * y1; e = y3 - y0 + h * y3; f = y0;
      }

      const H = [a, b, c, d, e, f, g, h, 1];
      const inv = invert3x3(H);
      if (!inv) return null;

      return {
        project(u, v) {
          const den = H[6] * u + H[7] * v + H[8];
          return { x: (H[0] * u + H[1] * v + H[2]) / den, y: (H[3] * u + H[4] * v + H[5]) / den };
        },
        unproject(x, y) {
          const den = inv[6] * x + inv[7] * y + inv[8];
          return { u: (inv[0] * x + inv[1] * y + inv[2]) / den, v: (inv[3] * x + inv[4] * y + inv[5]) / den };
        }
      };
    }

    function invert3x3(m) {
      const a = m[0], b = m[1], c = m[2], d = m[3], e = m[4], f = m[5], g = m[6], h = m[7], i = m[8];
      const A = e * i - f * h, B = -(d * i - f * g), C = d * h - e * g;
      const D = -(b * i - c * h), E = a * i - c * g, F = -(a * h - b * g);
      const G = b * f - c * e, H = -(a * f - c * d), I = a * e - b * d;
      const det = a * A + b * B + c * C;
      if (Math.abs(det) < 1e-6) return null;
      return [A / det, D / det, G / det, B / det, E / det, H / det, C / det, F / det, I / det];
    }

    function m2p(u, v) { return { u: 0.5 + (u - 0.5) / PLANE_SCALE, v: 0.5 + (v - 0.5) / PLANE_SCALE }; }
    function p2m(u, v) { return { u: 0.5 + (u - 0.5) * PLANE_SCALE, v: 0.5 + (v - 0.5) * PLANE_SCALE }; }

    function projectPlanePoint(track, u, v) {
      const projector = makeProjector(track.corners);
      if (!projector) return { x: 0, y: 0 };
      const marker = p2m(u, v);
      return projector.project(marker.u, marker.v);
    }

    function planePoly(track) {
      return [
        projectPlanePoint(track, 0, 0),
        projectPlanePoint(track, 1, 0),
        projectPlanePoint(track, 1, 1),
        projectPlanePoint(track, 0, 1)
      ];
    }

    function trackAt(x, y, fresh = true) {
      let best = null;
      let bestArea = -1;

      for (const track of visibleTracks()) {
        if (fresh && track.misses > 0) continue;
        const projector = makeProjector(track.corners);
        if (!projector) continue;

        const uv = projector.unproject(x, y);
        const plane = m2p(uv.u, uv.v);

        if (plane.u >= -0.08 && plane.u <= 1.08 && plane.v >= -0.08 && plane.v <= 1.08) {
          const area = polygonArea(track.corners);
          if (area > bestArea) {
            bestArea = area;
            best = track;
          }
        }
      }

      return best;
    }

    function pointerToCanvas(event) {
      const rect = canvas.getBoundingClientRect();
      return {
        x: (event.clientX - rect.left) * canvas.width / rect.width,
        y: (event.clientY - rect.top) * canvas.height / rect.height
      };
    }

    function onPointerDown(event) {
      event.preventDefault();
      pointerDown = true;
      lastPointer = pointerToCanvas(event);
      canvas.setPointerCapture(event.pointerId);
      pendingFirstPoint = null;

      if (eraserMode) {
        beginErase();
        erasePoint(lastPointer.x, lastPointer.y);
        return;
      }

      const track = trackAt(lastPointer.x, lastPointer.y, true);
      if (track) {
        activeKey = track.key;
        currentStroke = null;
        addPoint(lastPointer.x, lastPointer.y);
      } else {
        currentStroke = null;
      }

      updateModeUI();
    }

    function onPointerMove(event) {
      lastPointer = pointerToCanvas(event);
      if (!pointerDown) return;
      event.preventDefault();

      if (eraserMode) erasePoint(lastPointer.x, lastPointer.y);
      else addPoint(lastPointer.x, lastPointer.y);
    }

    function onPointerUp() {
      pointerDown = false;
      cleanupShortStroke(activeKey, currentStroke);
      currentStroke = null;
      pendingFirstPoint = null;
      finishErase();
    }

    function confirmFirst(key, u, v, x, y) {
      if (!pendingFirstPoint || pendingFirstPoint.key !== key) {
        pendingFirstPoint = { key, u, v, x, y, count: 1 };
        return false;
      }

      const uvDist = Math.hypot(u - pendingFirstPoint.u, v - pendingFirstPoint.v);
      const screenDist = Math.hypot(x - pendingFirstPoint.x, y - pendingFirstPoint.y);

      if (uvDist <= CONFIRM_FIRST_POINT_UV_RADIUS && screenDist <= CONFIRM_FIRST_POINT_SCREEN_RADIUS) {
        pendingFirstPoint.u = (pendingFirstPoint.u + u) * 0.5;
        pendingFirstPoint.v = (pendingFirstPoint.v + v) * 0.5;
        pendingFirstPoint.x = (pendingFirstPoint.x + x) * 0.5;
        pendingFirstPoint.y = (pendingFirstPoint.y + y) * 0.5;
        pendingFirstPoint.count++;
      } else {
        pendingFirstPoint = { key, u, v, x, y, count: 1 };
        return false;
      }

      return pendingFirstPoint.count >= CONFIRM_FIRST_POINT_FRAMES;
    }

    function addPoint(x, y) {
      const track = trackAt(x, y, true);
      if (!track) {
        pendingFirstPoint = null;
        return;
      }

      if (track.key !== activeKey) {
        activeKey = track.key;
        currentStroke = null;
        pendingFirstPoint = null;
      }

      const projector = makeProjector(track.corners);
      if (!projector) return;

      const uv = projector.unproject(x, y);
      const plane = m2p(uv.u, uv.v);

      if (plane.u < -0.15 || plane.u > 1.15 || plane.v < -0.15 || plane.v > 1.15) {
        pendingFirstPoint = null;
        return;
      }

      const u = Math.max(0, Math.min(1, plane.u));
      const v = Math.max(0, Math.min(1, plane.v));

      if (!currentStroke) {
        if (!confirmFirst(activeKey, u, v, x, y)) return;

        currentStroke = {
          color: [...brushColor],
          size: brushSize,
          points: [{ u: pendingFirstPoint.u, v: pendingFirstPoint.v }]
        };

        getStrokes(activeKey).push(currentStroke);
        actionHistory.push({ type: "stroke", key: activeKey, stroke: currentStroke });
        pendingFirstPoint = null;
        return;
      }

      if (!currentStroke.points.length) return;

      const last = currentStroke.points[currentStroke.points.length - 1];
      const jump = Math.hypot(u - last.u, v - last.v);
      if (jump > MAX_UV_JUMP) return;
      if (jump > 0.003) currentStroke.points.push({ u, v });
    }

    function strokeLength(stroke) {
      if (!stroke || stroke.points.length < 2) return 0;
      let length = 0;
      for (let i = 1; i < stroke.points.length; i++) {
        const a = stroke.points[i - 1];
        const b = stroke.points[i];
        length += Math.hypot(b.u - a.u, b.v - a.v);
      }
      return length;
    }

    function cleanupShortStroke(key, stroke) {
      if (!key || !stroke) return;
      if (stroke.points.length >= 2 && strokeLength(stroke) >= 0.004) return;

      const strokes = getStrokes(key);
      const idx = strokes.indexOf(stroke);
      if (idx >= 0) strokes.splice(idx, 1);

      for (let i = actionHistory.length - 1; i >= 0; i--) {
        if (actionHistory[i].type === "stroke" && actionHistory[i].stroke === stroke) {
          actionHistory.splice(i, 1);
          break;
        }
      }
    }

    function cloneStrokes(strokes) {
      return strokes.map(s => ({
        color: [...s.color],
        size: s.size,
        points: s.points.map(p => ({ u: p.u, v: p.v }))
      }));
    }

    function beginErase() {
      eraserSnapshot = new Map();
      eraserChanged = false;
      for (const [key, strokes] of strokesByMarker.entries()) {
        eraserSnapshot.set(key, cloneStrokes(strokes));
      }
    }

    function finishErase() {
      if (eraserChanged && eraserSnapshot) actionHistory.push({ type: "erase", data: eraserSnapshot });
      eraserSnapshot = null;
      eraserChanged = false;
    }

    function erasePoint(x, y) {
      const track = trackAt(x, y, true);
      if (!track) return;

      activeKey = track.key;
      const projector = makeProjector(track.corners);
      if (!projector) return;

      const uv = projector.unproject(x, y);
      const plane = m2p(uv.u, uv.v);

      if (plane.u < -0.08 || plane.u > 1.08 || plane.v < -0.08 || plane.v > 1.08) return;

      const radius = Math.max(0.025, brushSize / 650);
      const strokes = getStrokes(track.key);
      let changed = false;
      const newStrokes = [];

      for (const stroke of strokes) {
        let segment = [];
        const strokeRadius = radius + stroke.size / 900;

        for (const point of stroke.points) {
          if (Math.hypot(point.u - plane.u, point.v - plane.v) <= strokeRadius) {
            changed = true;
            if (segment.length >= 2) newStrokes.push({ color: stroke.color, size: stroke.size, points: segment });
            segment = [];
          } else {
            segment.push(point);
          }
        }

        if (segment.length >= 2) newStrokes.push({ color: stroke.color, size: stroke.size, points: segment });
      }

      if (changed) {
        strokesByMarker.set(track.key, newStrokes);
        eraserChanged = true;
      }

      updateModeUI();
    }

    function applyTexture(key, textureName, record = true) {
      const old = texturesByMarker.has(key) ? texturesByMarker.get(key) : null;
      texturesByMarker.set(key, textureName);
      if (record) actionHistory.push({ type: "texture", key, old });
      updateModeUI();
    }

    function removeTexture(key, record = true) {
      const old = texturesByMarker.has(key) ? texturesByMarker.get(key) : null;
      texturesByMarker.delete(key);
      if (record) actionHistory.push({ type: "texture", key, old });
      updateModeUI();
    }

    function clearFace(key, record = true) {
      const old = { strokes: cloneStrokes(getStrokes(key)), texture: texturesByMarker.has(key) ? texturesByMarker.get(key) : null };
      strokesByMarker.set(key, []);
      texturesByMarker.delete(key);
      if (record) actionHistory.push({ type: "clearFace", key, old });
      updateModeUI();
    }

    function clearAll(record = true) {
      const old = { strokes: new Map(), textures: new Map(texturesByMarker) };
      for (const [key, strokes] of strokesByMarker.entries()) old.strokes.set(key, cloneStrokes(strokes));
      strokesByMarker.clear();
      texturesByMarker.clear();
      if (record) actionHistory.push({ type: "clearAll", old });
      updateModeUI();
    }

    function undo() {
      const action = actionHistory.pop();
      if (!action) {
        toast("Nothing to undo.");
        return;
      }

      if (action.type === "stroke") {
        const strokes = getStrokes(action.key);
        if (strokes.length) strokes.pop();
      } else if (action.type === "texture") {
        action.old === null ? texturesByMarker.delete(action.key) : texturesByMarker.set(action.key, action.old);
      } else if (action.type === "clearFace") {
        strokesByMarker.set(action.key, cloneStrokes(action.old.strokes));
        action.old.texture === null ? texturesByMarker.delete(action.key) : texturesByMarker.set(action.key, action.old.texture);
      } else if (action.type === "clearAll") {
        strokesByMarker = action.old.strokes;
        texturesByMarker = action.old.textures;
      } else if (action.type === "erase") {
        strokesByMarker = action.data;
      }

      updateModeUI();
    }

    function setEraser(value) {
      eraserMode = value;
      currentStroke = null;
      pendingFirstPoint = null;
      updateModeUI();
    }

    function initUI() {
      for (const [key, color, name] of COLORS) {
        const div = document.createElement("button");
        div.className = "color" + (key === "1" ? " active" : "");
        div.style.background = `rgb(${color[0]}, ${color[1]}, ${color[2]})`;
        div.title = name;
        div.addEventListener("click", () => {
          brushColor = [...color];
          brushName = name;
          setEraser(false);
          updateBrushUI();
          updateColorUI();
        });
        colorsEl.appendChild(div);
      }

      for (const [name, texCanvas] of textures.entries()) {
        const div = document.createElement("div");
        div.className = "material" + (name === currentTextureName ? " active" : "");
        div.dataset.name = name;

        const preview = texCanvas.cloneNode();
        preview.width = texCanvas.width;
        preview.height = texCanvas.height;
        preview.getContext("2d").drawImage(texCanvas, 0, 0);

        const dots = document.createElement("div");
        dots.className = "drag-dots";
        dots.innerHTML = "<i></i><i></i><i></i><i></i>";

        const label = document.createElement("div");
        label.className = "material-label";
        label.textContent = name;

        div.appendChild(preview);
        div.appendChild(dots);
        div.appendChild(label);

        div.addEventListener("click", () => {
          currentTextureName = name;
          updateMaterialUI();
          updateModeUI();
        });

        div.addEventListener("pointerdown", event => dragTexture(event, name, texCanvas));
        materialsEl.appendChild(div);
      }
    }

    function updateMaterialUI() {
      document.querySelectorAll(".material").forEach(el => {
        el.classList.toggle("active", el.dataset.name === currentTextureName);
      });
    }

    function updateColorUI() {
      document.querySelectorAll(".color").forEach((el, i) => {
        el.classList.toggle("active", COLORS[i][2] === brushName && !eraserMode);
      });
    }

    function updateBrushUI() {
      brushSlider.value = String(brushSize);
      brushSizeText.textContent = String(brushSize);
      const dotSize = Math.max(4, Math.min(30, brushSize));
      brushDot.style.width = `${dotSize}px`;
      brushDot.style.height = `${dotSize}px`;
      brushDot.style.background = `rgb(${brushColor[0]}, ${brushColor[1]}, ${brushColor[2]})`;
    }

    function updateModeUI() {
      const face = activeKey ? `ID ${idFromKey(activeKey)}` : "NONE";
      modeText.textContent = `${eraserMode ? "ERASER" : "DRAW"} / FACE ${face}`;
      selectedText.textContent = `${draggingTextureName ? "Dragging" : "Selected"}: ${draggingTextureName || currentTextureName} | ${lastDetectionInfo}`;
      drawBtn.classList.toggle("active", !eraserMode);
      eraserBtn.classList.toggle("active", eraserMode);
      updateMaterialUI();
      updateColorUI();
      updateBrushUI();
    }

    function dragTexture(event, name, texCanvas) {
      event.preventDefault();
      draggingTextureName = name;
      currentTextureName = name;
      lastPointer = clientToCanvas(event.clientX, event.clientY);
      updateModeUI();

      ghost.style.display = "block";
      ghost.innerHTML = "";

      const clone = texCanvas.cloneNode();
      clone.width = texCanvas.width;
      clone.height = texCanvas.height;
      clone.getContext("2d").drawImage(texCanvas, 0, 0);
      ghost.appendChild(clone);
      moveGhost(event.clientX, event.clientY);

      const move = ev => {
        lastPointer = clientToCanvas(ev.clientX, ev.clientY);
        moveGhost(ev.clientX, ev.clientY);
      };

      const up = ev => {
        document.removeEventListener("pointermove", move);
        document.removeEventListener("pointerup", up);
        ghost.style.display = "none";

        const p = clientToCanvas(ev.clientX, ev.clientY);
        if (p) {
          const track = trackAt(p.x, p.y, false);
          if (track) {
            activeKey = track.key;
            applyTexture(track.key, draggingTextureName, true);
          } else {
            toast("Drop material on a visible cube face.");
          }
        }

        draggingTextureName = null;
        updateModeUI();
      };

      document.addEventListener("pointermove", move);
      document.addEventListener("pointerup", up);
    }

    function moveGhost(x, y) {
      ghost.style.left = `${x + 12}px`;
      ghost.style.top = `${y + 12}px`;
    }

    function clientToCanvas(x, y) {
      const rect = canvas.getBoundingClientRect();
      if (x < rect.left || x > rect.right || y < rect.top || y > rect.bottom) return null;
      return {
        x: (x - rect.left) * canvas.width / rect.width,
        y: (y - rect.top) * canvas.height / rect.height
      };
    }

    function render() {
      ctx.clearRect(0, 0, canvas.width, canvas.height);

      const sorted = visibleTracks().sort((a, b) => polygonArea(a.corners) - polygonArea(b.corners));
      for (const track of sorted) drawTrack(track);

      if (draggingTextureName && lastPointer) {
        const track = trackAt(lastPointer.x, lastPointer.y, false);
        if (track) drawTexture(track, draggingTextureName, 0.55);
        drawDragTextureCursor(lastPointer.x, lastPointer.y, draggingTextureName);
      }

      if (debugMode) drawDebug();
      drawBrushPreview();

      requestAnimationFrame(render);
    }

    function drawTrack(track) {
      if (texturesByMarker.has(track.key)) drawTexture(track, texturesByMarker.get(track.key), TEXTURE_ALPHA);

      const strokes = strokesByMarker.get(track.key) || [];
      for (const stroke of strokes) drawStroke(track, stroke);
    }

    function drawStroke(track, stroke) {
      if (!stroke.points || stroke.points.length < 2) return;

      ctx.save();
      ctx.strokeStyle = `rgb(${stroke.color[0]}, ${stroke.color[1]}, ${stroke.color[2]})`;
      ctx.lineWidth = stroke.size;
      ctx.lineCap = "round";
      ctx.lineJoin = "round";

      ctx.beginPath();
      stroke.points.forEach((pt, index) => {
        const p = projectPlanePoint(track, pt.u, pt.v);
        if (index === 0) ctx.moveTo(p.x, p.y);
        else ctx.lineTo(p.x, p.y);
      });
      ctx.stroke();
      ctx.restore();
    }

    function drawTexture(track, textureName, alpha) {
      const img = textures.get(textureName);
      if (!img) return;

      const quad = planePoly(track);
      ctx.save();
      ctx.globalAlpha = alpha;
      drawQuad(ctx, img, quad);
      ctx.restore();
    }

    function drawQuad(context, image, quad) {
      const w = image.width;
      const h = image.height;
      drawTriangle(context, image, 0, 0, w, 0, w, h, quad[0], quad[1], quad[2]);
      drawTriangle(context, image, 0, 0, w, h, 0, h, quad[0], quad[2], quad[3]);
    }

    function drawTriangle(c, img, sx0, sy0, sx1, sy1, sx2, sy2, d0, d1, d2) {
      c.save();
      c.beginPath();
      c.moveTo(d0.x, d0.y);
      c.lineTo(d1.x, d1.y);
      c.lineTo(d2.x, d2.y);
      c.closePath();
      c.clip();

      const den = sx0 * (sy1 - sy2) + sx1 * (sy2 - sy0) + sx2 * (sy0 - sy1);
      if (Math.abs(den) < 1e-6) {
        c.restore();
        return;
      }

      const a = (d0.x * (sy1 - sy2) + d1.x * (sy2 - sy0) + d2.x * (sy0 - sy1)) / den;
      const b = (d0.y * (sy1 - sy2) + d1.y * (sy2 - sy0) + d2.y * (sy0 - sy1)) / den;
      const cc = (d0.x * (sx2 - sx1) + d1.x * (sx0 - sx2) + d2.x * (sx1 - sx0)) / den;
      const d = (d0.y * (sx2 - sx1) + d1.y * (sx0 - sx2) + d2.y * (sx1 - sx0)) / den;
      const e = (d0.x * (sx1 * sy2 - sx2 * sy1) + d1.x * (sx2 * sy0 - sx0 * sy2) + d2.x * (sx0 * sy1 - sx1 * sy0)) / den;
      const f = (d0.y * (sx1 * sy2 - sx2 * sy1) + d1.y * (sx2 * sy0 - sx0 * sy2) + d2.y * (sx0 * sy1 - sx1 * sy0)) / den;

      c.setTransform(a, b, cc, d, e, f);
      c.drawImage(img, 0, 0);
      c.restore();
    }

    function drawDragTextureCursor(x, y, name) {
      const img = textures.get(name);
      if (!img) return;

      const s = DRAG_PREVIEW_SIZE;
      ctx.save();
      ctx.globalAlpha = 0.92;
      ctx.drawImage(img, x - s / 2, y - s / 2, s, s);
      ctx.globalAlpha = 1;
      ctx.strokeStyle = "#98dc00";
      ctx.lineWidth = 3;
      ctx.strokeRect(x - s / 2, y - s / 2, s, s);
      ctx.strokeStyle = "#fff";
      ctx.lineWidth = 2;
      ctx.beginPath();
      ctx.moveTo(x - 15, y);
      ctx.lineTo(x + 15, y);
      ctx.moveTo(x, y - 15);
      ctx.lineTo(x, y + 15);
      ctx.stroke();
      ctx.font = "bold 15px Arial";
      ctx.lineWidth = 4;
      ctx.strokeStyle = "#000";
      ctx.fillStyle = "#98dc00";
      ctx.strokeText("DROP ON FACE", x - 48, y + s / 2 + 22);
      ctx.fillText("DROP ON FACE", x - 48, y + s / 2 + 22);
      ctx.restore();
    }

    function drawDebug() {
      ctx.save();
      ctx.lineWidth = 2;
      ctx.strokeStyle = "#98dc00";
      ctx.fillStyle = "#98dc00";
      ctx.font = "15px Arial";

      for (const track of visibleTracks()) {
        const p = track.corners;
        ctx.beginPath();
        ctx.moveTo(p[0].x, p[0].y);
        for (let i = 1; i < p.length; i++) ctx.lineTo(p[i].x, p[i].y);
        ctx.closePath();
        ctx.stroke();
        ctx.fillText(String(track.id), p[0].x, p[0].y - 8);
      }

      ctx.restore();
    }

    function drawBrushPreview() {
      if (eraserMode || performance.now() > brushPreviewUntil) return;

      ctx.save();
      const x = 90, y = 90;
      ctx.fillStyle = `rgb(${brushColor[0]}, ${brushColor[1]}, ${brushColor[2]})`;
      ctx.strokeStyle = "white";
      ctx.lineWidth = 2;
      ctx.beginPath();
      ctx.arc(x, y, Math.max(2, brushSize / 2), 0, Math.PI * 2);
      ctx.fill();
      ctx.stroke();
      ctx.font = "18px Arial";
      ctx.fillStyle = "white";
      ctx.strokeStyle = "black";
      ctx.lineWidth = 4;
      ctx.strokeText(`Brush ${brushSize}`, x - 36, y + 48);
      ctx.fillText(`Brush ${brushSize}`, x - 36, y + 48);
      ctx.restore();
    }

    function showBrushPreview() {
      brushPreviewUntil = performance.now() + 1250;
    }

    function initTextures() {
      textures.set("Grass", texGrass());
      textures.set("Wood", texWood());
      textures.set("Stone", texStone());
      textures.set("Sand", texSand());
      textures.set("Water", texWater());
      textures.set("Glass", texGlass());
      textures.set("Metal", texMetal());
      textures.set("Leaf", texLeaf());
      textures.set("Clay", texClay());
    }

    function makeCanvas(size = 256) {
      const c = document.createElement("canvas");
      c.width = size;
      c.height = size;
      return c;
    }

    function texNoise(base, strength) {
      const c = makeCanvas();
      const cx = c.getContext("2d");
      const image = cx.createImageData(256, 256);
      for (let i = 0; i < image.data.length; i += 4) {
        image.data[i] = clamp(base[0] + random(-strength, strength), 0, 255);
        image.data[i + 1] = clamp(base[1] + random(-strength, strength), 0, 255);
        image.data[i + 2] = clamp(base[2] + random(-strength, strength), 0, 255);
        image.data[i + 3] = 255;
      }
      cx.putImageData(image, 0, 0);
      return c;
    }

    function texGrass() {
      const c = texNoise([45, 125, 55], 35);
      const cx = c.getContext("2d");
      for (let i = 0; i < 220; i++) {
        cx.strokeStyle = ["#23a046", "#36bf55", "#196b2d", "#52d36a"][Math.floor(Math.random() * 4)];
        cx.beginPath();
        const x = random(0, 256), y = random(0, 256);
        cx.moveTo(x, y);
        cx.lineTo(x + random(-5, 5), y - random(12, 34));
        cx.stroke();
      }
      return c;
    }

    function texWood() {
      const c = makeCanvas();
      const cx = c.getContext("2d");
      for (let y = 0; y < 256; y++) {
        for (let x = 0; x < 256; x++) {
          const g = 0.5 + 0.5 * Math.sin(x / 8 + 0.7 * Math.sin(y / 18));
          const r = 0.5 + 0.5 * Math.sin((x + y * 0.25) / 20);
          const v = 0.65 * g + 0.35 * r;
          cx.fillStyle = `rgb(${120 + v * 85},${75 + v * 75},${35 + v * 45})`;
          cx.fillRect(x, y, 1, 1);
        }
      }
      return c;
    }

    function texStone() { return texNoise([120, 120, 115], 55); }
    function texSand() { return texNoise([220, 190, 120], 28); }

    function texWater() {
      const c = makeCanvas();
      const cx = c.getContext("2d");
      for (let y = 0; y < 256; y++) {
        for (let x = 0; x < 256; x++) {
          const v = 0.65 * (0.5 + 0.5 * Math.sin(x / 10 + Math.sin(y / 18) * 2)) + 0.35 * (0.5 + 0.5 * Math.sin((x + y) / 22));
          cx.fillStyle = `rgb(${20 + v * 55},${80 + v * 90},${140 + v * 100})`;
          cx.fillRect(x, y, 1, 1);
        }
      }
      return c;
    }

    function texGlass() {
      const c = makeCanvas();
      const cx = c.getContext("2d");
      const g = cx.createLinearGradient(0, 0, 256, 256);
      g.addColorStop(0, "#dcefff");
      g.addColorStop(0.45, "#b9d3e3");
      g.addColorStop(1, "#f6fdff");
      cx.fillStyle = g;
      cx.fillRect(0, 0, 256, 256);
      cx.strokeStyle = "rgba(255,255,255,.75)";
      cx.lineWidth = 3;
      for (let i = -256; i < 256; i += 44) {
        cx.beginPath();
        cx.moveTo(i, 256);
        cx.lineTo(i + 256, 0);
        cx.stroke();
      }
      return c;
    }

    function texMetal() {
      const c = makeCanvas();
      const cx = c.getContext("2d");
      const g = cx.createLinearGradient(0, 0, 0, 256);
      g.addColorStop(0, "#777");
      g.addColorStop(0.5, "#d0d3d6");
      g.addColorStop(1, "#666");
      cx.fillStyle = g;
      cx.fillRect(0, 0, 256, 256);
      for (let y = 0; y < 256; y += 5) {
        const v = Math.floor(random(115, 220));
        cx.strokeStyle = `rgb(${v},${v},${v + 10})`;
        cx.beginPath();
        cx.moveTo(0, y);
        cx.lineTo(256, y + random(-1, 1));
        cx.stroke();
      }
      return c;
    }

    function texLeaf() {
      const c = texNoise([35, 145, 70], 25);
      const cx = c.getContext("2d");
      cx.strokeStyle = "#78dc78";
      cx.lineWidth = 2;
      cx.beginPath();
      cx.moveTo(128, 256);
      cx.lineTo(128, 0);
      cx.stroke();
      for (let y = 20; y < 256; y += 24) {
        cx.beginPath();
        cx.moveTo(128, y);
        cx.lineTo(20, y - 30);
        cx.moveTo(128, y);
        cx.lineTo(236, y - 30);
        cx.stroke();
      }
      return c;
    }

    function texClay() { return texNoise([170, 105, 80], 38); }

    function random(a, b) { return Math.random() * (b - a) + a; }
    function clamp(v, a, b) { return Math.max(a, Math.min(b, v)); }

    async function toggleFullscreen() {
      try {
        if (!document.fullscreenElement) await document.documentElement.requestFullscreen();
        else await document.exitFullscreen();
      } catch {
        toast("Fullscreen not available.");
      }
    }

    function handleKey(event) {
      const k = event.key.toLowerCase();

      if (k >= "1" && k <= "9") {
        const c = COLORS[Number(k) - 1];
        brushColor = [...c[1]];
        brushName = c[2];
        setEraser(false);
        updateBrushUI();
        updateColorUI();
      } else if (k === "e") setEraser(true);
      else if (k === "p") setEraser(false);
      else if (k === "u") undo();
      else if (k === "x") clearAll(true);
      else if (k === "c" && activeKey) clearFace(activeKey, true);
      else if ((k === "t" || k === "f") && activeKey) applyTexture(activeKey, currentTextureName, true);
      else if (k === "y" && activeKey) removeTexture(activeKey, true);
      else if (k === "[") {
        brushSize = Math.max(2, brushSize - 1);
        updateBrushUI();
        showBrushPreview();
      } else if (k === "]") {
        brushSize = Math.min(52, brushSize + 1);
        updateBrushUI();
        showBrushPreview();
      }
    }

    function toast(message) {
      messageBox.textContent = message;
      messageBox.style.display = "block";
      clearTimeout(toast._timer);
      toast._timer = setTimeout(() => messageBox.style.display = "none", 4200);
    }
  </script>
</body>
</html>
