from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from services.image_services import generate_image
import time

app = FastAPI()
last_req_time=0
DEMO_COOLDOWN_SECONDS = 60

# CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class ImageRequest(BaseModel):
    prompt: str

@app.get("/health")
def health():
    return {"status": "ok"}

@app.post("/generate-image")
async def create_image(request: ImageRequest):
    global last_req_time

    current_time = time.time()

    # Demo rate limit protection
    if current_time - last_req_time < DEMO_COOLDOWN_SECONDS:
        remaining = int(DEMO_COOLDOWN_SECONDS - (current_time - last_req_time))
        return {
            "message": f"Demo mode: please wait {remaining} seconds before generating another image."
        }

    try:
        image = generate_image(request.prompt)
        last_req_time = time.time()
        return {"image": image}

    except Exception:
        
        return {
            "message": "Image generation temporarily unavailable (demo quota limit). Please try again later."
        }

