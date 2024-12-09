from transformers import AutoModelForCausalLM, AutoTokenizer
from PIL import Image

def questionMoondream2(image_path,question):
    model_id = "vikhyatk/moondream2"
    revision = "2024-08-26"
    model = AutoModelForCausalLM.from_pretrained(
        model_id, trust_remote_code=True, revision=revision
    )
    tokenizer = AutoTokenizer.from_pretrained(model_id, revision=revision)

    image = Image.open(image_path)
    enc_image = model.encode_image(image)
    rep = model.answer_question(enc_image, question, tokenizer)
    return rep