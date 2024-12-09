import torch
from transformers import AutoModel, AutoTokenizer

# Set up the model and tokenizer
path = 'OpenGVLab/InternVL2-1B'
model = AutoModel.from_pretrained(
    path,
    torch_dtype=torch.bfloat16,
    low_cpu_mem_usage=True,
    use_flash_attn=True,
    trust_remote_code=True).eval().cuda()
tokenizer = AutoTokenizer.from_pretrained(path, trust_remote_code=True, use_fast=False)

print("\n==SUCCESS==\n")