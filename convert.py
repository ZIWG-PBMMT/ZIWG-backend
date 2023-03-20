import base64
import cv2
import numpy as np


def b64_to_img(b64_string: str) -> np.ndarray:
    b64_string = b64_string.encode('utf-8')
    im_bytes = base64.b64decode(b64_string)
    im_arr = np.frombuffer(im_bytes, dtype=np.uint8)
    img = cv2.imdecode(im_arr, flags=cv2.IMREAD_COLOR)
    return img
