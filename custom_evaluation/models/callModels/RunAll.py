from models.callModels.InternVL2_1B import questionInternVL2_1B, open_InternVL2_1B
from models.callModels.Kosmos2 import questionKosmos2, open_Kosmos2
from models.callModels.MiniCPMV2 import questionMiniCPMV2, open_MiniCPMV2
from models.callModels.Mississippi import questionMississippi, open_Mississipi
from models.callModels.Moondream2 import questionMoondream2, open_Moondream2
from utils.videos_modifications import videos_quality, videos_modifications
import json
from PIL import Image
import torch

def questionALLwrite(image_path, question, times):
    list_Moondream2 = []
    list_InternVL2_1B = []
    list_Kosmos2 = []
    list_MiniCPMV2 = []
    list_Mississipi = []
    

    model_Moondream2, tokenizer_Moondrem2 = open_Moondream2()
    for quality in videos_quality:
        for modification in videos_modifications:
            for i, time in enumerate(times):
                path = f"frames/{quality}_{modification}/frame{i+1}_{time}.png"
                image = Image.open(path)
                list_Moondream2.append(dict(video = f"{quality}_{modification}",frame_id = i+1, text = questionMoondream2(question, model_Moondream2, tokenizer_Moondrem2, image)))
                
    torch.cuda.empty_cache()
    with open("Moondream2.json", "w") as outfile:
        json.dump(list_Moondream2, outfile)
    outfile.close()
    print("== Moondream2 SUCCESS ==")

    model_InternVL2, tokenizer_InternVL2 = open_InternVL2_1B()
    for quality in videos_quality:
        for modification in videos_modifications:
            for i, time in enumerate(times):
                path = f"frames/{quality}_{modification}/frame{i+1}_{time}.png"
                image_rgb = Image.open(path).convert('RGB')
                list_InternVL2_1B.append(dict(video = f"{quality}_{modification}", frame_id = i+1, text = questionInternVL2_1B(question, model_InternVL2, tokenizer_InternVL2, image_rgb)))
    
    torch.cuda.empty_cache()
    with open("InternVL2_1B.json", "w") as outfile:
        json.dump(list_InternVL2_1B, outfile)
    outfile.close()
    print("== InternVL2 SUCCESS ==")
    
    model_Kosmos2, processor_Komos2, device_Kosmos2 = open_Kosmos2()
    for quality in videos_quality:
        for modification in videos_modifications:
            for i, time in enumerate(times):
                path = f"frames/{quality}_{modification}/frame{i+1}_{time}.png"
                image = Image.open(path)
                list_Kosmos2.append(dict(video = f"{quality}_{modification}", frame_id = i+1, text = questionKosmos2(question, model_Kosmos2, processor_Komos2, device_Kosmos2, image)))
                
    
    with open("Kosmos2.json", "w") as outfile:
        json.dump(list_Kosmos2, outfile)
    outfile.close()
    print("== Kosmos2 SUCCESS ==")
    
    model_MiniCPMV2, tokenizer_MiniCPMV2 = open_MiniCPMV2()
    for quality in videos_quality:
        for modification in videos_modifications:
            for i, time in enumerate(times):
                path = f"frames/{quality}_{modification}/frame{i+1}_{time}.png"
                image_rgb = Image.open(path).convert('RGB')
                list_MiniCPMV2.append(dict(video = f"{quality}_{modification}", frame_id = i+1, text = questionMiniCPMV2(question, model_MiniCPMV2, tokenizer_MiniCPMV2, image_rgb)))

    torch.cuda.empty_cache()           
    with open("MiniCPMV2.json", "w") as outfile:
        json.dump(list_MiniCPMV2, outfile)
    outfile.close()
    print("== MiniCPMV2 SUCCESS ==")
    
    model_Mississipi, tokenizer_Mississipi, generation_config_Mississipi = open_Mississipi()
    for quality in videos_quality:
        for modification in videos_modifications:
            for i, time in enumerate(times):
                path = f"frames/{quality}_{modification}/frame{i+1}_{time}.png"
                list_Mississipi.append(dict(video = f"{quality}_{modification}", frame_id = i+1, text = questionMississippi(path, question, model_Mississipi, tokenizer_Mississipi, generation_config_Mississipi)))

    torch.cuda.empty_cache()   
    with open("Mississipi.json", "w") as outfile:
        json.dump(list_Mississipi, outfile)
    outfile.close()
    print("== Mississippi SUCCESS ==")

    print("Les réponses ont été écrites dans les fichiers json")