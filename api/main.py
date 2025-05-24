from fastapi import FastAPI,File,UploadFile
import uvicorn
import numpy as np
from io import BytesIO
from PIL import Image
import tensorflow as tf



# When you go to http://localhost:8000 in your browser,
# you're trying to connect to a web server that should be running on your own computer, listening on port 8000.


app = FastAPI()
MODEL = tf.keras.models.load_model("../saved_models/1")
CLASS_NAMES = ["Early Blight","Late Blight","Healthy"]


def read_file_as_image(data) -> np.ndarray:
    image = np.array(Image.open(BytesIO(data)))
    return image
@app.post("/predict")
async def predict(
        file: UploadFile = File(...)
):
    image = read_file_as_image(await file.read())
    img_batch = np.expand_dims(image,0)

    prediction = MODEL.predict(img_batch)

    predicted_class = CLASS_NAMES[np.argmax(prediction[0])]
    confidence = np.max(prediction[0])

    return {
        'class': predicted_class,
        'confidence' : float(confidence)
    }
if __name__ == "__main__":
    uvicorn.run(app,host='localhost',port=8000)
    # Runs the app using Uvicorn, a fast ASGI server.
    # Binds the server to localhost on port 8000.