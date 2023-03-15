from fastapi import FastAPI
from pydantic import BaseModel

import settings
from ai_controller import AIController


class Gesture(BaseModel):
    expected_gesture: str
    gesture: str


app = FastAPI()
ai = AIController(settings.paths.get("model_path"))


@app.get("/")
async def root():
    return {"message": "Please use valid POST endpoint ({base_url}/gestures/"}


@app.post("/gestures/")
async def create_photo(gesture: Gesture):
    return ai.is_gesture_correct(gesture.expected_gesture, gesture.gesture)
