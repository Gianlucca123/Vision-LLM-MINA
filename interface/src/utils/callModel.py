from utils.InternVL2_1B import questionInternVL2_1B, open_InternVL2_1B
from PIL import Image
import os
import torch
import markdown
from datetime import datetime, timezone
from utils.logs import write_logs

def get_answer_InternVL2_1B(cache_path, prompt, max_token_length, log_file_path, fps):
    """
    @brief Generates answers using the InternVL2-1B model for images in the cache directory.
    This function loads the InternVL2-1B model and tokenizer, iterates over all image files in the specified cache directory,
    generates answers for each image based on the provided prompt, and yields the results in a specific format.
    @param cache_path The path to the directory containing cached image files.
    @param prompt The prompt to be used for generating answers.
    @param max_token_length The maximum token length for the generated answers.
    @return Yields a formatted string containing the frame ID and the generated answer for each image.
    @note The function clears the CUDA cache after processing all images.
    """

    model_InternVL2, tokenizer_InternVL2 = open_InternVL2_1B()

    # iterate over all files in the cache directory
    for i, name in enumerate(sorted(os.listdir(cache_path))):
        path = os.path.join(cache_path, name)
        image_rgb = Image.open(path).convert("RGB")
        answer = questionInternVL2_1B(
            prompt, model_InternVL2, tokenizer_InternVL2, image_rgb, max_token_length
        )

        # remove the .jpg from name and remove the leading zeros (except if the name is 0)
        name = name[:-4].lstrip("0")
        if name == "":
            name = "0"

        # compute the timestamp using int(name)
        timestamp = int(name) / fps
        timestamp = str(
            datetime.fromtimestamp(timestamp, timezone.utc).strftime("%H:%M:%S")
        )

        # write the answer to the logs
        write_logs(answer, timestamp, name, log_file_path)

        answer = answer.replace("'", "guillemetsimple").replace('"', "guillemetdouble")
        answer = markdown.markdown(answer)

        yield f"data: {dict(frame_id=name, answer=answer)}\n\n"

    # clear the cache
    torch.cuda.empty_cache()
