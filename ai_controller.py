import random

import numpy as np
from convert import b64_to_img
import torch
import torchvision.transforms as transforms


class AIController:
    def __init__(self, ai_model_path):
        self.ai_model_path = ai_model_path
        self.ai_model = None
        self.device = torch.device('cuda') if torch.cuda.is_available() else torch.device('cpu')
        # self.load_ai_model()

    def load_ai_model(self):
        if self.ai_model is None:
            self.ai_model = torch.load(self.ai_model_path, map_location=self.device)
            self.ai_model.eval()
            self.ai_model = self.ai_model.to(self.device)

            """torch.load(self.ai_model_path, map_location=self.device)
            self.ai_model.eval()
            self.ai_model = self.ai_model.to(self.device)
            
            W przypadku PyTorch wygląda to tak jak powyżej. Zaimplementować w zależoności od modelu.
            Ten komentarz można usunąć i zamienić na właściwy kod. 
            Komentarze w poniższych funkcjach pełnią rolę dokumentacji.
            """

    def is_gesture_correct(self, expected_gesture: str, gesture: str) -> bool:
        """
        convert gesture base64 string to np.ndarray img
        pass img to AI and receive decision what is it
        check if AI decision and expected are the same

        return result of check
        """
        # img = b64_to_img(gesture)
        # print(type(img))
        # ai_decision = self.recognize_img_label_by_ai(img)
        # is_expected = expected_gesture == ai_decision
        # return is_expected
        # CODE ABOVE IS COMMENTED BECAUSE AI MODEL DOEST NOT EXIST
        return True if random.randint(0, 1) else False

    def recognize_img_label_by_ai(self, img: np.ndarray) -> str:
        """
        pass img to AI model and receive recognized label

        return label
        """
        # torch.from_numpy(img)
        img = get_transform_test()(img).unsqueeze(0)
        img = img.to(self.device)
        raw_result = self.ai_model.forward(img)
        result = torch.nn.functional.softmax(raw_result, dim=1)
        confidence, decision = torch.max(result, 1)
        return str(decision)


def get_transform_test(input_required_size=224):
    return transforms.Compose([
        transforms.Resize((input_required_size, input_required_size)),
        transforms.CenterCrop(input_required_size),
        transforms.ToTensor(),
        transforms.Normalize(mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225]),
    ])

