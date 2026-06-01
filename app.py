from fastapi import FastAPI
from pydantic import BaseModel
import torch

app = FastAPI()

# Load model once during startup
print("Loading WAN model...")

# Replace with actual WAN loading code
model = None

class GenerateRequest(BaseModel):
    prompt: str
    negative_prompt: str = ""
    num_frames: int = 81

@app.get("/")
def health():
    return {
        "status": "running",
        "model_loaded": model is not None
    }

@app.post("/generate")
async def generate_video(req: GenerateRequest):

    if model is None:
        return {
            "success": False,
            "message": "Model not loaded"
        }

    # Replace with WAN inference
    output_path = "/tmp/output.mp4"

    return {
        "success": True,
        "video_path": output_path
    }
