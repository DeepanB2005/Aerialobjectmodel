from fastapi import FastAPI, UploadFile, File
from fastapi.responses import FileResponse
from fastapi.middleware.cors import CORSMiddleware
from ultralytics import YOLO
import os, zipfile, shutil

app = FastAPI()

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],  # Or specify your frontend URL
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

model = YOLO("yolov8x-obb.pt")  # High-accuracy model

UPLOAD_DIR = "uploads"
RESULT_DIR = "results"

os.makedirs(UPLOAD_DIR, exist_ok=True)
os.makedirs(RESULT_DIR, exist_ok=True)

@app.post("/annotate")
async def annotate_images(files: list[UploadFile] = File(...)):
    # Clear previous results
    shutil.rmtree(UPLOAD_DIR, ignore_errors=True)
    shutil.rmtree(RESULT_DIR, ignore_errors=True)
    os.makedirs(UPLOAD_DIR, exist_ok=True)
    os.makedirs(RESULT_DIR, exist_ok=True)

    # Save uploaded images
    for file in files:
        with open(f"{UPLOAD_DIR}/{file.filename}", "wb") as f:
            f.write(await file.read())

    # Run YOLOv8-OBB inference
    model.predict(
        source=UPLOAD_DIR,
        conf=0.15,
        imgsz=1280,
        save=True,
        project=RESULT_DIR,
        name="predictions"
    )

    # Zip the annotated results
    zip_path = "annotations.zip"
    with zipfile.ZipFile(zip_path, 'w') as zipf:
        for root, _, files in os.walk(f"{RESULT_DIR}/predictions"):
            for file in files:
                zipf.write(os.path.join(root, file),
                           os.path.relpath(os.path.join(root, file),
                           f"{RESULT_DIR}/predictions"))

    return FileResponse(zip_path, media_type='application/zip', filename="annotations.zip")

@app.get("/")
def home():
    return {"message": "YOLOv8-OBB Aerial Image Annotation API"}
