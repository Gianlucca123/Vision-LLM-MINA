import requests
from transformers import AutoProcessor, AutoModelForVision2Seq

# Set up the model and processor
model = AutoModelForVision2Seq.from_pretrained("microsoft/kosmos-2-patch14-224")
processor = AutoProcessor.from_pretrained("microsoft/kosmos-2-patch14-224")

print("\n==SUCCESS==\n")