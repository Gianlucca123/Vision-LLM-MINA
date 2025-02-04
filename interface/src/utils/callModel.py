from utils.InternVL2_1B import questionInternVL2_1B, open_InternVL2_1B
from PIL import Image
import os
import torch
import markdown

def get_answer_InternVL2_1B(cache_path, prompt, max_token_length):
    model_InternVL2, tokenizer_InternVL2 = open_InternVL2_1B()

    # iterate over all files in the cache directory
    for i, name in enumerate(sorted(os.listdir(cache_path))):
        path = os.path.join(cache_path, name)
        image_rgb = Image.open(path).convert('RGB')
        answer = questionInternVL2_1B(prompt, model_InternVL2, tokenizer_InternVL2, image_rgb, max_token_length)

        # remove the .jpg from name and remove the leading zeros (except if the name is 0)
        name = name[:-4].lstrip("0")
        if name == "":
            name = "0"

        answer = answer.replace("'", "guillemetsimple").replace('"', "guillemetdouble")
        answer = markdown.markdown(answer)  

        yield f"data: {dict(frame_id = name, answer = answer)}\n\n"
    
    # clear the cache
    torch.cuda.empty_cache()