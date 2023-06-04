from pydantic import BaseModel, Field


class Gesture(BaseModel):
    expected_gesture: str
    gesture: str
    is_correct: bool = Field(None)
