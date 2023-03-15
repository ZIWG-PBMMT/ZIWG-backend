import time

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

import settings
from ai_controller import AIController


class Gesture(BaseModel):
    expected_gesture: str
    gesture: str


app = FastAPI()
ai = AIController(settings.paths.get("model_path"))

origins = [
    "*"
]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
async def root():
    return {"message": "Please use valid POST endpoint ({base_url}/gestures/"}


@app.post("/gestures/")
async def create_photo(gesture: Gesture):
    is_gesture_correct = ai.is_gesture_correct(gesture.expected_gesture, gesture.gesture)
    return {"is_gesture_correct": f"{is_gesture_correct}"}
    # return{"is_gesture_correct": f"{gesture.expected_gesture == gesture.gesture}"}        # for react learning
