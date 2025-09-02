AI-Assisted Aerial Image Annotation Tool

An AI-powered web application for automated annotation of aerial imagery using YOLOv8-OBB (Oriented Bounding Boxes).
This tool pre-labels objects such as trees, buildings, lakes, and water bodies with confidence scores, allowing human annotators to validate and correct labels efficiently, reducing manual annotation time by at least 50%.

Project Thesis
Problem

Annotating aerial images manually is time-consuming and labor-intensive, especially for large datasets (e.g., 10–50 images per batch).

Solution

An AI-assisted annotation tool that:

Uses a trained YOLOv8-OBB model for automatic object detection in aerial images.

Pre-labels objects with confidence scores.

Allows users to quickly review, edit, or correct labels through a web interface.

Expected Outcome

50% reduction in annotation time compared to manual labeling.

High-quality annotations ready for training advanced object detection models.

Features

Automated object detection for:



Batch image processing (10–50 images at once)

Adjustable detection thresholds (confidence & NMS)

Downloadable YOLO-format labels

Interactive web interface built with React + Flask/FastAPI backend

Tech Stack

Frontend: React (Vite)

Backend: FastAPI (Python)

AI Model: YOLOv8-OBB (yolov8x-obb.pt for high accuracy)

Frameworks & Libraries: ultralytics, numpy, opencv-python

Deployment: Docker-ready (optional: Render, Vercel, or your server)

Installation
Prerequisites

Python ≥ 3.9

Node.js ≥ 18

pip ≥ 23.0

1. Clone the Repository
git clone https://github.com/DeepanB2005/Aerialobjectmodel.git
cd Aerialobjectmodel

## 2. Backend Setup

cd bc
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt

Example requirements.txt
fastapi
uvicorn
ultralytics
opencv-python
numpy
pillow


Run the backend:

uvicorn main:app --host 0.0.0.0 --port 8000 --reload

## 3. Frontend Setup
cd fr
npm install
npm run dev


This starts the frontend on:

http://localhost:5173

Usage

Upload a batch of aerial images (10–50 images).

Click "Annotate" – The model will:

Run YOLOv8-OBB predictions.

Pre-label objects with bounding boxes & confidence scores.

Review and adjust annotations if necessary.

Download the labels in YOLO format.

Customization

To modify detection classes:
Edit the YOLOv8 configuration file in models/custom.yaml.

To change confidence/NMS thresholds:
Adjust in backend/config.py:

CONF_THRESHOLD = 0.15
NMS_THRESHOLD = 0.4

Expected Annotation Workflow

AI Pre-annotation → 2. Human Validation/Correction → 3. Export Labels → 4. Train Your Custom Model

Future Enhancements

Support for multi-scale detection for extremely small/large objects.

Integration with Roboflow or CVAT for large-scale labeling.

Cloud deployment (AWS/GCP/Azure).

License

This project is licensed under the MIT License.