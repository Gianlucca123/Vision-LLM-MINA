import torch
from transformers import AutoModel, AutoTokenizer

# Set up the model and tokenizer
model_path = 'h2oai/h2ovl-mississippi-2b'
model = AutoModel.from_pretrained(
    model_path,
    torch_dtype=torch.bfloat16,
    low_cpu_mem_usage=True,
    trust_remote_code=True).eval().cuda()
tokenizer = AutoTokenizer.from_pretrained(model_path, trust_remote_code=True, use_fast=False)

print("\n==SUCCESS==\n")