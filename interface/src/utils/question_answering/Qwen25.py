from transformers import AutoTokenizer, AutoModelForCausalLM
import torch

def open_Qwen05():
    """
    @brief Loads the Qwen2.5-0.5B-Instruct model and tokenizer.
    This function initializes and loads the Qwen2.5-0.5B-Instruct model and its corresponding tokenizer 
    from the Hugging Face model hub. The model is moved to the GPU for faster inference.
    @return A tuple containing the tokenizer and the model.
    """
    tokenizer = AutoTokenizer.from_pretrained("Qwen/Qwen2.5-0.5B-Instruct")
    model = AutoModelForCausalLM.from_pretrained("Qwen/Qwen2.5-0.5B-Instruct").to("cuda")
    return tokenizer, model

def open_Qwen15():
    """
    @brief Loads the Qwen 2.5-1.5B Instruct model and tokenizer.
    This function initializes and loads the Qwen 2.5-1.5B Instruct model and its corresponding tokenizer 
    from the Hugging Face model hub. The model is moved to the GPU for faster inference.
    @return A tuple containing:
        - tokenizer: The tokenizer for the Qwen 2.5-1.5B Instruct model.
        - model: The Qwen 2.5-1.5B Instruct model loaded on the GPU.
    """
    tokenizer = AutoTokenizer.from_pretrained("Qwen/Qwen2.5-1.5B-Instruct")
    model = AutoModelForCausalLM.from_pretrained("Qwen/Qwen2.5-1.5B-Instruct").to("cuda")
    return tokenizer, model

def questionQwen(prompt, tokenizer, model):
    """
    @brief Generates an answer to a given prompt using a specified tokenizer and model.
    @param prompt The input text prompt to generate an answer for.
    @param tokenizer The tokenizer to preprocess the input text.
    @param model The model to generate the answer.
    @return The generated answer as a string.
    """   
    input_text = prompt
    inputs = tokenizer(input_text, return_tensors="pt", padding=True, truncation=True)
    input_ids = inputs.input_ids.to("cuda")
    attention_mask = inputs.attention_mask.to("cuda")  # <- Explicitly create attention mask

    outputs = model.generate(input_ids, attention_mask=attention_mask, max_new_tokens=100)

    answer = tokenizer.decode(outputs[0], skip_special_tokens=True)

    return answer

def clean_cuda(model, tokenizer):
    """
    @brief Cleans up CUDA resources by emptying the GPU cache and deleting the model and tokenizer.
    This function performs the following steps:
    - Empties the GPU cache using torch.cuda.empty_cache().
    - Collects any outstanding GPU memory using torch.cuda.ipc_collect().
    - Deletes the provided model and tokenizer to free up memory.
    @param model The model to be deleted.
    @param tokenizer The tokenizer to be deleted.
    """
    # clear the cache
    torch.cuda.empty_cache()
    torch.cuda.ipc_collect()
    del model
    del tokenizer
    