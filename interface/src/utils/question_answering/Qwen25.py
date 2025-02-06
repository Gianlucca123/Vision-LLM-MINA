from transformers import AutoTokenizer, AutoModelForCausalLM
import torch

def open_Qwen05():
    tokenizer = AutoTokenizer.from_pretrained("Qwen/Qwen2.5-0.5B-Instruct")
    model = AutoModelForCausalLM.from_pretrained("Qwen/Qwen2.5-0.5B-Instruct").to("cuda")
    return tokenizer, model

def open_Qwen15():
    tokenizer = AutoTokenizer.from_pretrained("Qwen/Qwen2.5-1.5B-Instruct")
    model = AutoModelForCausalLM.from_pretrained("Qwen/Qwen2.5-1.5B-Instruct").to("cuda")
    return tokenizer, model

def questionQwen(prompt, tokenizer, model):
    input_text = prompt
    inputs = tokenizer(input_text, return_tensors="pt", padding=True, truncation=True)
    input_ids = inputs.input_ids.to("cuda")
    attention_mask = inputs.attention_mask.to("cuda")  # <- Explicitly create attention mask

    outputs = model.generate(input_ids, attention_mask=attention_mask, max_length=32768)

    answer = tokenizer.decode(outputs[0], skip_special_tokens=True)

    return answer

def clean_cuda():
    # Vider le cache GPU
    torch.cuda.empty_cache()
    torch.cuda.ipc_collect()