from PIL import Image
from convert import b64_to_img
import torch
import constants
import torchvision.transforms as transforms


class AIController:
    def __init__(self):
        self.model = torch.load(constants.MODEL_PATH)
        self.model.eval()
        self.model.to("cpu")

    def is_gesture_correct(self, expected_gesture: str, gesture: str) -> bool:
        """
        convert gesture base64 string to np.ndarray img
        pass img to AI and receive decision what is it
        check if AI decision and expected are the same

        return result of check
        """
        return expected_gesture == self.recognize_img(b64_to_img(gesture))

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


def get_transform(input_required_size=224):
    return transforms.Compose(
        [
            transforms.Resize((input_required_size, input_required_size)),
            transforms.CenterCrop(input_required_size),
            transforms.ToTensor(),
            transforms.Normalize(mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225]),
        ]
    )
