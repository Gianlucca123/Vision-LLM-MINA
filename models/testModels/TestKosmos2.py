import requests
import torch
from PIL import Image
from transformers import AutoProcessor, AutoModelForVision2Seq

# Check if GPU is available
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

# Load the model and processor
model = AutoModelForVision2Seq.from_pretrained("microsoft/kosmos-2-patch14-224").to(device)
processor = AutoProcessor.from_pretrained("microsoft/kosmos-2-patch14-224")

prompt = "Describe this image."

# Load the image
image = Image.open("Img1.jpg")

# Process the inputs
inputs = processor(text=prompt, images=image, return_tensors="pt")

# Move the inputs to the GPU
inputs = {key: value.to(device) for key, value in inputs.items()}

# Generate the output
generated_ids = model.generate(
    pixel_values=inputs["pixel_values"],
    input_ids=inputs["input_ids"],
    attention_mask=inputs["attention_mask"],
    image_embeds=None,
    image_embeds_position_mask=inputs["image_embeds_position_mask"],
    use_cache=True,
    max_new_tokens=128,
)

# Decode the generated text
generated_text = processor.batch_decode(generated_ids, skip_special_tokens=True)[0]

# Specify `cleanup_and_extract=False` in order to see the raw model generation.
processed_text = processor.post_process_generation(generated_text, cleanup_and_extract=False)

# By default, the generated text is cleaned up and the entities are extracted.
processed_text, entities = processor.post_process_generation(generated_text)

print(processed_text)
# `An image of a snowman warming himself by a fire.`

#print(entities)
# `[('a snowman', (12, 21), [(0.390625, 0.046875, 0.984375, 0.828125)]), ('a fire', (41, 47), [(0.171875, 0.015625, 0.484375, 0.890625)])]`
