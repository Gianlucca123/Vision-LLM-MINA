import torch
from transformers import AutoModel, AutoTokenizer
from huggingface_hub import login
from dotenv import load_dotenv
import os

# Replace 'token' with your access token
load_dotenv()
token = os.getenv('HUGGINGFACE_HUB_TOKEN')
login(token)

# Set up the model and tokenizer
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

print("\n==SUCCESS==\n")