from utils.InternVL2_1B import questionInternVL2_1B, open_InternVL2_1B
from PIL import Image
import os

def get_answer_InternVL2_1B(cache_path):
    list_InternVL2_1B = []
    model_InternVL2, tokenizer_InternVL2 = open_InternVL2_1B()

    # iterate over all files in the cache directory
    for i, name in enumerate(os.listdir(cache_path)):
        path = os.path.join(cache_path, name)
        image_rgb = Image.open(path).convert('RGB')
        answer = questionInternVL2_1B("You are an expert at analyzing real world images. Describe all you see on this picture.", model_InternVL2, tokenizer_InternVL2, image_rgb)
        list_InternVL2_1B.append(dict(frame_id = name, text = answer))
        print(f"question asked for frame name {name}")

    return list_InternVL2_1B