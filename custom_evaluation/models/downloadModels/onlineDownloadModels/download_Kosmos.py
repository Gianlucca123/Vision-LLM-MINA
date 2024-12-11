import requests
import torch
from transformers import AutoProcessor, AutoModelForVision2Seq

# Check if GPU is available
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

# Set up the model and processor
model = AutoModelForVision2Seq.from_pretrained("microsoft/kosmos-2-patch14-224").to(device)
processor = AutoProcessor.from_pretrained("microsoft/kosmos-2-patch14-224")

print("\n==SUCCESS==\n")