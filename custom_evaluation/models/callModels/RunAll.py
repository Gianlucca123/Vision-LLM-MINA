from .InternVL2_1B import questionInternVL2_1B
from .Kosmos2 import questionKosmos2
from .MiniCPMV2 import questionMiniCPMV2
from .Mississippi import questionMississippi
from .Moondream2 import questionMoondream2
from .Qwen2_VL_2B_Instruct import questionQwen2VL2B
from ...utils.videos_modifications import videos_quality, videos_modifications
import json

def questionALLwrite(image_path, question, times):
    list_Moondream2 = []
    list_InternVL2_1B = []
    list_Kosmos2 = []
    list_MiniCPMV2 = []
    list_Mississipi = []
    list_Qwen2VL2B = []
    
    for quality in videos_quality:
        for modification in videos_modifications:
            for i, time in enumerate(times):
                path = f"../../frames/{quality}_{modification}/frame{i+1}_{time}.png"

                list_Moondream2.append(dict(frame_id = i+1, text = questionMoondream2(path, question)))
                list_InternVL2_1B.append(dict(frame_id = i+1, text = questionInternVL2_1B(path, question)))
                list_Kosmos2.append(dict(frame_id = i+1, text = questionKosmos2(path, question)))
                list_MiniCPMV2.append(dict(frame_id = i+1, text = questionMiniCPMV2(path, question)))
                list_Mississipi.append(dict(frame_id = i+1, text = questionMississippi(path, question)))
                list_Qwen2VL2B.append(dict(frame_id = i+1, text = questionQwen2VL2B(path, question)))

    with open("Moondream2.json", "w") as outfile:
        json.dump(list_Moondream2, outfile)

    outfile.close()

    with open("InternVL2_1B.json", "w") as outfile:
        json.dump(list_InternVL2_1B, outfile)

    outfile.close()

    with open("Kosmos2.json", "w") as outfile:
        json.dump(list_Kosmos2, outfile)

    outfile.close()

    with open("MiniCPMV2.json", "w") as outfile:
        json.dump(list_MiniCPMV2, outfile)

    outfile.close()

    with open("Mississipi.json", "w") as outfile:
        json.dump(list_Mississipi, outfile)

    outfile.close()

    with open("Qwen2VL2B.json", "w") as outfile:
        json.dump(list_Qwen2VL2B, outfile)

    outfile.close()



    """ with open("responses.txt", "w") as file:
        file.write("Moondream2 :\n" + questionMoondream2(image_path, question) + "\n\n") #Moondream2 sometimes causes a Kill
        file.write("InternVL2_1B :\n" + questionInternVL2_1B(image_path, question) + "\n\n")
        file.write("Kosmos2 :\n" + questionKosmos2(image_path, question) + "\n\n")
        file.write("MiniCPMV2 :\n" + questionMiniCPMV2(image_path, question) + "\n\n")
        file.write("Mississippi :\n" + questionMississippi(image_path, question) + "\n\n")
        file.write("Qwen2VL2B :\n" + questionQwen2VL2B(image_path, question) + "\n\n") """

    print("Les réponses ont été écrites dans les fichiers json")