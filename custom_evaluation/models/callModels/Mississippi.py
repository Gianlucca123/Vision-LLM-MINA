import torch
from transformers import AutoModel, AutoTokenizer


def questionMississippi(image_path,question):
    model_path = 'h2oai/h2ovl-mississippi-2b'
    model = AutoModel.from_pretrained(
        model_path,
        torch_dtype=torch.bfloat16,
        low_cpu_mem_usage=True,
        trust_remote_code=True).eval().cuda()
    tokenizer = AutoTokenizer.from_pretrained(model_path, trust_remote_code=True, use_fast=False)
    generation_config = dict(max_new_tokens=1024, do_sample=True)

    response, history = model.chat(tokenizer, image_path, question, generation_config, history=None, return_history=True)
    return response