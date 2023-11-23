from io import BytesIO

from fastapi import FastAPI, UploadFile, File
from PIL import Image

from .model import Model


app = FastAPI()
model = Model()


@app.post("/infer")
async def infer(image_file: UploadFile = File(...)):
    # Read image file
    image_data = await image_file.read()
    image = Image.open(BytesIO(image_data))

    # Call model for inference
    result = model(image)
    return {"result": result}


@app.get("/health")
async def health():
    return {"status": "ok"}
