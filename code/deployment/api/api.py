import os
from fastapi import FastAPI, UploadFile, File
from fastapi.responses import JSONResponse
from models.model import BrainTumorDetector
import uvicorn
from PIL import Image
import io


app = FastAPI()

model_path = os.path.join('models', 'model_0.pt')
data_path = os.path.join('data', 'data.yaml')
detector = BrainTumorDetector(model_path, data_path)


def delete_image(image_path):
    if os.path.exists(image_path):
        os.remove(image_path)
    else:
        print(f"File not found: {image_path}")


@app.post("/predict")
async def predict(file: UploadFile = File(...)):
    contents = await file.read()
    image = Image.open(io.BytesIO(contents))
    temp_dir = os.path.join('data', 'temp.jpg')

    image.save(temp_dir)
    result = detector.detect(temp_dir)
    delete_image(temp_dir)
    
    return JSONResponse(content={"prediction": result})
