import torch
from torchvision import transforms
from torch.utils.data import DataLoader, Dataset
from PIL import Image
import os

class ImageDataset(Dataset):
    def __init__(self, root_dir):
        self.root_dir = root_dir
        self.transform = transforms.Compose([
                            transforms.Resize((224, 224)),
                            transforms.ToTensor(),
                            transforms.Normalize([0.5, 0.5, 0.5], [0.5, 0.5, 0.5])
                        ])
        self.image_list = os.listdir(root_dir)
        
    def __len__(self):
        return len(self.image_list)
        
    def __getitem__(self, idx):
        img_path = os.path.join(self.root_dir, self.image_list[idx])
        image = Image.open(img_path)
        image = self.transform(image)
        return image

image_dataset = ImageDataset('images')
dataloader = DataLoader(image_dataset, batch_size=32, shuffle=True)
