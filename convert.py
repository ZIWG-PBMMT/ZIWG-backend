import base64
from PIL import Image, ImageEnhance
from io import BytesIO


def b64_to_img(b64_string: str) -> Image.Image:
    img_bytes = base64.b64decode(b64_string)
    img = Image.open(BytesIO(img_bytes)).convert("RGB")
    # img.show()
    return img


def rbh_to_grayscale(img: Image.Image) -> Image.Image:
    img_filter = ImageEnhance.Color(img)
    img_filter.enhance(0)
    return img
