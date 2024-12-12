import torch
from PIL import Image
from transformers import AutoModel, AutoTokenizer
from huggingface_hub import login
from dotenv import load_dotenv
import os

def open_MiniCPMV2():
    load_dotenv()
    token = os.getenv('HUGGINGFACE_HUB_TOKEN')

    # Replace 'token' with your access token
    login(token)

    model_id = "openbmb/MiniCPM-V-2"
    trust_remote_code = True

    model = AutoModel.from_pretrained(model_id, trust_remote_code=trust_remote_code, torch_dtype=torch.bfloat16)
    # For Nvidia GPUs support BF16 (like A100, H100, RTX3090)
    model = model.to(device='cuda', dtype=torch.bfloat16)
    # For Other setups check TestMiniCPMV2.py

    tokenizer = AutoTokenizer.from_pretrained(model_id, trust_remote_code=trust_remote_code)
    model.eval()
    return model, tokenizer

def questionMiniCPMV2(question, model, tokenizer, image):
    #image = Image.open(image_path).convert('RGB')
    msgs = [{'role': 'user', 'content': question}]

    res, context, _ = model.chat(
        image=image,
        msgs=msgs,
        context=None,
        tokenizer=tokenizer,
        sampling=True,
        temperature=0.7
    )
    return res

