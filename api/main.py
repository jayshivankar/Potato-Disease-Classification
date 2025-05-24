from fastapi import FastAPI,File,UploadFile
import uvicorn
# When you go to http://localhost:8000 in your browser,
# you're trying to connect to a web server that should be running on your own computer, listening on port 8000.


app = FastAPI()

@app.post("/predict")
async def predict(

)

if __name__ == "__main__":
    uvicorn.run(app,host='localhost',port=8000)
    # Runs the app using Uvicorn, a fast ASGI server.
    # Binds the server to localhost on port 8000.