from fastapi import FastAPI
from pydantic import BaseModel
import os

app = FastAPI()

class RequestData(BaseModel):
    prompt: str

@app.get("/")
def health():
    return {
        "status": "running"
    }

@app.post("/predict")
def predict(data: RequestData):
    result = {
        "output": f"Received: {data.prompt}"
    }
    return result

if __name__ == "__main__":
    import uvicorn

    port = int(os.environ.get("PORT", 8080))

    uvicorn.run(
        "app:app",
        host="0.0.0.0",
        port=port
    )
