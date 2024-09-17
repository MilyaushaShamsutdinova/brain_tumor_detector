import sys
import os

from fastapi import FastAPI, UploadFile, File
from fastapi.responses import JSONResponse
from models.model import BrainTumorDetector
import uvicorn
from PIL import Image
import io


app = FastAPI()

model_path = r'M:\python_projects\brain_tumor_detector\models\model_0.pt'
data_path = r'M:\python_projects\brain_tumor_detector\code\datasets\Brain-tumor-Detection-1\data.yaml'
detector = BrainTumorDetector(model_path, data_path)

@app.post("/predict")
async def predict(file: UploadFile = File(...)):
    contents = await file.read()
    image = Image.open(io.BytesIO(contents))
    temp_dir = r'M:\python_projects\brain_tumor_detector\data\temp_image.jpg'
    image.save(temp_dir)  # Saving image temporarily

    # Perform detection
    result = detector.detect(temp_dir)
    
    # Return result
    return JSONResponse(content={"prediction": result})

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
