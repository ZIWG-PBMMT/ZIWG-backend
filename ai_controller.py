import numpy as np
from convert import b64_to_img


class AIController:
    def __init__(self, ai_model_path):
        self.ai_model_path = ai_model_path
        self.ai_model = None

    def load_ai_model(self):
        pass

    def is_gesture_correct(self, expected_gesture: str, gesture: str) -> bool:
        img = b64_to_img(gesture)                                   # convert gesture base64 string to np.ndarray img
        ai_decision = self.recognize_img_label_by_ai(img)           # pass img to AI and receive decision what is it
        result = expected_gesture == ai_decision                    # check if AI decision and expected are the same
        return result

    def recognize_img_label_by_ai(self, img: np.ndarray) -> str:
        pass

