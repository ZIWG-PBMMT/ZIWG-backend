import torchvision.transforms as transforms


def get_transform(input_required_size=480):
    return transforms.Compose(
        [
            transforms.Resize((input_required_size, input_required_size)),
            transforms.CenterCrop(input_required_size),
            transforms.ToTensor(),
            transforms.Normalize(mean=[0.5], std=[0.5])
        ]
    )
