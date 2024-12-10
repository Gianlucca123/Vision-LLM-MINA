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
generation_config = dict(max_new_tokens=1024, do_sample=True)


# pure-text conversation
#question = 'Hello, who are you?'
#response, history = model.chat(tokenizer, None, question, generation_config, history=None, return_history=True)
#print(f'User: {question}\nAssistant: {response}')


# Example for single image
image_file = 'Img1.jpg'
question = "Describe this image."
response, history = model.chat(tokenizer, image_file, question, generation_config, history=None, return_history=True)
print(f'User: {question}\nAssistant: {response}')


# Example for multiple images - multiround conversation
#image_files = ['./examples/image1.jpg', './examples/image2.jpg']
#question = 'Image-1: <image>\nImage-2: <image>\nDescribe the Image-1 and Image-2 in detail.'
#response, history = model.chat(tokenizer, image_files, question, generation_config, history=None, return_history=True)
#print(f'User: {question}\nAssistant: {response}')

#question = 'What are the similarities and differences between these two images.'
#response, history = model.chat(tokenizer, image_files, question, generation_config=generation_config, history=history, return_history=True)
#print(f'User: {question}\nAssistant: {response}')
