from Moondream2 import questionMoondream2
from InternVL2_1B import questionInternVL2_1B
from Qwen2_VL_2B_Instruct import questionQwen2VL2B

def questionALLprint(image_path,question):
    print(questionMoondream2(image_path,question))
    print(questionInternVL2_1B(image_path,question))
    print(questionQwen2VL2B(image_path,question))

question = "Describe this image."
image_path = 'Img1.jpg'

questionALLprint(image_path,question)