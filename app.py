from fastapi import FastAPI, UploadFile, File, Form
from fastapi.responses import JSONResponse
import os
import torch

app = FastAPI()

MODEL_LOADED = False
pipe = None

@app.on_event("startup")
async def startup():

    global pipe
    global MODEL_LOADED

    try:
        from diffusers import DiffusionPipeline

        pipe = DiffusionPipeline.from_pretrained(
            "Wan-AI/Wan2.2-T2V-A14B",
            torch_dtype=torch.bfloat16
        )

        pipe.enable_model_cpu_offload()

        MODEL_LOADED = True

    except Exception as e:
        print(e)

@app.get("/")
def health():
    return {
        "status": "running",
        "model_loaded": MODEL_LOADED
    }

@app.post("/generate")
async def generate(
    prompt: str = Form(...)
):
    if not MODEL_LOADED:
        return JSONResponse(
            status_code=500,
            content={"error": "model not loaded"}
        )

    return {
        "success": True,
        "prompt": prompt
    }
