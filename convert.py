import base64
from PIL import Image
from io import BytesIO


def b64_to_img(b64_string: str) -> Image.Image:
    img_bytes = base64.b64decode(b64_string)
    img = Image.open(BytesIO(img_bytes)).convert("RGB")
    # img.show()
    return img
