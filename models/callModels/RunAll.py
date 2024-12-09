from InternVL2_1B import questionInternVL2_1B
from Kosmos2 import questionKosmos2
from MiniCPMV2 import questionMiniCPMV2
from Mississippi import questionMississippi
from Moondream2 import questionMoondream2
from Qwen2_VL_2B_Instruct import questionQwen2VL2B

def questionALLwrite(image_path, question):
    with open("responses.txt", "w") as file:
        file.write("InternVL2_1B :\n" + questionInternVL2_1B(image_path, question) + "\n\n")
        file.write("Kosmos2 :\n" + questionKosmos2(image_path, question) + "\n\n")
        file.write("MiniCPMV2 :\n" + questionMiniCPMV2(image_path, question) + "\n\n")
        file.write("Mississippi :\n" + questionMississippi(image_path, question) + "\n\n")
        file.write("Moondream2 :\n" + questionMoondream2(image_path, question) + "\n\n") #Moondream2 sometimes causes a Kill
        file.write("Qwen2VL2B :\n" + questionQwen2VL2B(image_path, question) + "\n\n")

    print("Les réponses ont été écrites dans le fichier responses.txt")
  

question = "Describe this image."
image_path = 'Img2.jpg'

questionALLwrite(image_path,question)