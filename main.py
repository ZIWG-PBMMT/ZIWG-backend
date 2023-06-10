from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware

import pickle
import uuid
from gesture import Gesture


app = FastAPI()

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
async def root():
    raise HTTPException(status_code=405, detail="Please use appropriate endpoint")


@app.get("/gestures/{gesture_uuid}")
async def get_gesture_result(gesture_uuid):
    try:
        with open(f"processed/gesture_{gesture_uuid}.pickle", "rb") as file:
            gesture: Gesture = pickle.load(file)
    except FileNotFoundError:
        return None
    return gesture.is_correct


@app.post("/gestures/")
async def create_photo(gesture: Gesture):
    react_prefix = "data:image/jpeg;base64,"
    gesture.gesture = gesture.gesture.removeprefix(react_prefix)
    gesture_uuid = str(uuid.uuid4())
    with open(f"to_be_processed/gesture_{gesture_uuid}.pickle", "wb") as file:
        pickle.dump(gesture, file)
    return gesture_uuid
