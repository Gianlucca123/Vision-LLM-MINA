from transformers import AutoModelForCausalLM, AutoTokenizer
from PIL import Image

def open_Moondream2():
    model_id = "vikhyatk/moondream2"
    revision = "2024-08-26"
    model = AutoModelForCausalLM.from_pretrained(
        model_id, trust_remote_code=True, revision=revision
    ).eval().cuda()
    tokenizer = AutoTokenizer.from_pretrained(model_id, revision=revision)
    return model, tokenizer

def questionMoondream2(question, model, tokenizer, image):
    #image = Image.open(image_path)
    enc_image = model.encode_image(image)
    rep = model.answer_question(enc_image, question, tokenizer)
    return rep