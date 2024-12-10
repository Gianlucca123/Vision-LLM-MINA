import requests
import torch
from PIL import Image
from transformers import AutoProcessor, AutoModelForVision2Seq

def questionKosmos2(image_path,question):
    # Check if GPU is available
    device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

    # Load the model and processor
    model = AutoModelForVision2Seq.from_pretrained("microsoft/kosmos-2-patch14-224").to(device)
    processor = AutoProcessor.from_pretrained("microsoft/kosmos-2-patch14-224")

    image = Image.open(image_path)

    inputs = processor(text=question, images=image, return_tensors="pt").to(device)

    generated_ids = model.generate(
        pixel_values=inputs["pixel_values"],
        input_ids=inputs["input_ids"],
        attention_mask=inputs["attention_mask"],
        image_embeds=None,
        image_embeds_position_mask=inputs["image_embeds_position_mask"],
        use_cache=True,
        max_new_tokens=128,
    )
    generated_text = processor.batch_decode(generated_ids, skip_special_tokens=True)[0]

    # Specify `cleanup_and_extract=False` in order to see the raw model generation.
    processed_text = processor.post_process_generation(generated_text, cleanup_and_extract=False)
    
    return processed_text
