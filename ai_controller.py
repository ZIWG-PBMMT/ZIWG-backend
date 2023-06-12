from PIL import Image
from convert import b64_to_img, rbh_to_grayscale
import torch
import constants
from transformations import get_transform


class AIController:
    def __init__(self):
        self.model = torch.load(constants.MODEL_PATH)
        self.model.eval()
        self.model.to("cpu")

    def is_gesture_correct(self, expected_gesture: str, gesture: str) -> bool:
        """
        convert gesture base64 string to PIL img
        pass img to AI as a grayscale img and receive decision what is it
        check if AI decision and expected are the same

        return result of check
        """
        return expected_gesture == self.recognize_img(rbh_to_grayscale(b64_to_img(gesture)))

    def recognize_img(self, img: Image.Image) -> str:
        """
        pass img to AI model and receive recognized label

        return label
        """
        tensor = get_transform()(img).unsqueeze(0)

        raw_result = self.model.forward(tensor)
        softmax_result = torch.nn.functional.softmax(raw_result, dim=1)
        confidence, prediction = torch.max(softmax_result, 1)

        return constants.SIGNS[int(prediction)]
