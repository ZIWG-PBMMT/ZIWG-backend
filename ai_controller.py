import base64
import time
import cv2
import numpy as np


def b64_to_img(b64_string: str) -> np.ndarray:
    b64_string = b64_string.encode('utf-8')
    im_bytes = base64.b64decode(b64_string)
    im_arr = np.frombuffer(im_bytes, dtype=np.uint8)
    img = cv2.imdecode(im_arr, flags=cv2.IMREAD_COLOR)
    return img


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

