import torch
from PIL import Image
from transformers import AutoModel, AutoTokenizer
from huggingface_hub import login
from dotenv import load_dotenv
import os

load_dotenv()
token = os.getenv('HUGGINGFACE_HUB_TOKEN')

# Replace 'your_huggingface_token' with your access token
login(token)

model_id = "openbmb/MiniCPM-V-2"
trust_remote_code = True

model = AutoModel.from_pretrained(model_id, trust_remote_code=trust_remote_code, torch_dtype=torch.bfloat16)
# For Nvidia GPUs support BF16 (like A100, H100, RTX3090)
model = model.to(device='cuda', dtype=torch.bfloat16)
# For Nvidia GPUs do NOT support BF16 (like V100, T4, RTX2080)
#model = model.to(device='cuda', dtype=torch.float16)
# For Mac with MPS (Apple silicon or AMD GPUs).
# Run with `PYTORCH_ENABLE_MPS_FALLBACK=1 python test.py`
#model = model.to(device='mps', dtype=torch.float16)

tokenizer = AutoTokenizer.from_pretrained(model_id, trust_remote_code=trust_remote_code)
model.eval()

image = Image.open('Img1.jpg').convert('RGB')
question = "Describe this image."
msgs = [{'role': 'user', 'content': question}]

res, context, _ = model.chat(
    image=image,
    msgs=msgs,
    context=None,
    tokenizer=tokenizer,
    sampling=True,
    temperature=0.7
)
print(res)

