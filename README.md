# Build Your Case - Vercel Python Version

This version runs on Vercel and still uses Python for ArUco detection.

## How it works

- Phone/PC browser uses its own camera.
- Browser sends a small JPEG frame to `/api/detect`.
- Python serverless function uses OpenCV ArUco detection.
- Browser renders textures, drawings, eraser, undo and UI.

## Deploy to Vercel

1. Upload this folder to GitHub.
2. Import the repo in Vercel.
3. Framework preset: Other.
4. Deploy.

Or with Vercel CLI:

```bash
npm i -g vercel
vercel
vercel --prod
```

## Important

Python/OpenCV on Vercel is slower than your local desktop app. This version is made for phone/PC accessibility, not maximum FPS.

Best settings:
- Use strong lighting.
- Keep markers large in view.
- Use the Balanced or Fast mode in the UI.
- Use a stable internet connection.

## Environment variables

Optional:

```text
ARUCO_DICTIONARY=DICT_4X4_50
CUBE_FACE_IDS=0,1,2,3,4,5
```

`CUBE_FACE_IDS` limits detection to your cube IDs.
