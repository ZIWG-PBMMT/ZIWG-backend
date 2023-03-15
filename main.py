from fastapi import FastAPI
from pydantic import BaseModel


class Gesture(BaseModel):
    expected_gesture: str
    gesture: str


app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Please use valid POST endpoint ({base_url}/gestures/"}


@app.post("/gestures/")
async def create_photo(gesture: Gesture):
    return gesture
