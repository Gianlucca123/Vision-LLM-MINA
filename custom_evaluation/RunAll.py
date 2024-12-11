from models.callModels.InternVL2_1B import questionInternVL2_1B, open_InternVL2_1B
from models.callModels.Kosmos2 import questionKosmos2, open_Kosmos2
from models.callModels.MiniCPMV2 import questionMiniCPMV2, open_MiniCPMV2
from models.callModels.Mississippi import questionMississippi, open_Mississippi
from models.callModels.Moondream2 import questionMoondream2, open_Moondream2
from models.callModels.Qwen2VL_2B import questionQwen2VL_2B, open_Qwen2VL_2B
from utils.videos_modifications import videos_quality, videos_modifications
import json
from PIL import Image
import torch
import argparse
import os

def main():    
    parser = argparse.ArgumentParser(
        description="Generate a Json file with the result of the model specified"
    )

    parser.add_argument(
        "--model",
        type=str,
        default="Moondrem2",
        help="Model that the script is going to use.",
    )

    parser.add_argument(
        "--question",
        type=str,
        default="Describe this image.",
        help="Question to the model.",
    )

    parser.add_argument(
        "--input_frames",
        type=str,
        default="frames",
        help="Path to the frames.",
    )

    parser.add_argument(
        "--result_output",
        type=str,
        default="results",
        help="Name of the directory where the results are going to be stored.",
    )


    args = parser.parse_args()

    # Create a directory called to store the results, if it does not already exist.
    try:
        os.mkdir(args.result_output)
        print(f"Directory '{args.result_output}' created successfully.")
    except FileExistsError:
        print(f"Directory '{args.result_output}' already exists.")


    match args.model:
        case "Moondrem2":
            list_Moondream2 = []
            model_Moondream2, tokenizer_Moondrem2 = open_Moondream2()
            for quality in videos_quality:
                for modification in videos_modifications:
                    for i, name in enumerate(os.listdir(os.path.join(args.input_frames,f"{quality}_{modification}"))):
                        path = os.path.join(args.input_frames,f"{quality}_{modification}", name)
                        image = Image.open(path)
                        list_Moondream2.append(dict(video = f"{quality}_{modification}",frame_id = i+1, text = questionMoondream2(args.question, model_Moondream2, tokenizer_Moondrem2, image)))
                        
            torch.cuda.empty_cache()
            with open(os.path.join(args.result_output,"Moondream2.json"), "w") as outfile:
                json.dump(list_Moondream2, outfile)
            outfile.close()
            print("== Moondream2 SUCCESS ==")

        case "InternVL2_1B":
            list_InternVL2_1B = []
            model_InternVL2, tokenizer_InternVL2 = open_InternVL2_1B()
            for quality in videos_quality:
                for modification in videos_modifications:
                    for i, name in enumerate(os.listdir(os.path.join(args.input_frames,f"{quality}_{modification}"))):
                        path = os.path.join(args.input_frames,f"{quality}_{modification}", name)
                        image_rgb = Image.open(path).convert('RGB')
                        list_InternVL2_1B.append(dict(video = f"{quality}_{modification}", frame_id = i+1, text = questionInternVL2_1B(args.question, model_InternVL2, tokenizer_InternVL2, image_rgb)))
            
            torch.cuda.empty_cache()
            with open(os.path.join(args.result_output,"InternVL2_1B.json"), "w") as outfile:
                json.dump(list_InternVL2_1B, outfile)
            outfile.close()
            print("== InternVL2_1B SUCCESS ==")

        case "Kosmos2":
            list_Kosmos2 = []
            model_Kosmos2, processor_Komos2, device_Kosmos2 = open_Kosmos2()
            for quality in videos_quality:
                for modification in videos_modifications:
                    for i, name in enumerate(os.listdir(os.path.join(args.input_frames,f"{quality}_{modification}"))):
                        path = os.path.join(args.input_frames,f"{quality}_{modification}", name)
                        image = Image.open(path)
                        list_Kosmos2.append(dict(video = f"{quality}_{modification}", frame_id = i+1, text = questionKosmos2(args.question, model_Kosmos2, processor_Komos2, device_Kosmos2, image)))
                        
            
            with open(os.path.join(args.result_output,"Kosmos2.json"), "w") as outfile:
                json.dump(list_Kosmos2, outfile)
            outfile.close()
            print("== Kosmos2 SUCCESS ==")

        case "MiniCPMV2":
            list_MiniCPMV2 = []
            model_MiniCPMV2, tokenizer_MiniCPMV2 = open_MiniCPMV2()
            for quality in videos_quality:
                for modification in videos_modifications:
                    for i, name in enumerate(os.listdir(os.path.join(args.input_frames,f"{quality}_{modification}"))):
                        path = os.path.join(args.input_frames,f"{quality}_{modification}", name)
                        image_rgb = Image.open(path).convert('RGB')
                        list_MiniCPMV2.append(dict(video = f"{quality}_{modification}", frame_id = i+1, text = questionMiniCPMV2(args.question, model_MiniCPMV2, tokenizer_MiniCPMV2, image_rgb)))

            torch.cuda.empty_cache()           
            with open(os.path.join(args.result_output,"MiniCPMV2.json"), "w") as outfile:
                json.dump(list_MiniCPMV2, outfile)
            outfile.close()
            print("== MiniCPMV2 SUCCESS ==")

        case "Mississippi":
            list_Mississippi = []
            model_Mississippi, tokenizer_Mississippi, generation_config_Mississippi = open_Mississippi()
            for quality in videos_quality:
                for modification in videos_modifications:
                    for i, name in enumerate(os.listdir(os.path.join(args.input_frames,f"{quality}_{modification}"))):
                        path = os.path.join(args.input_frames,f"{quality}_{modification}", name)
                        list_Mississippi.append(dict(video = f"{quality}_{modification}", frame_id = i+1, text = questionMississippi(path, args.question, model_Mississippi, tokenizer_Mississippi, generation_config_Mississippi)))

            torch.cuda.empty_cache()   
            with open(os.path.join(args.result_output,"Mississippi.json"), "w") as outfile:
                json.dump(list_Mississippi, outfile)
            outfile.close()
            print("== Mississippi SUCCESS ==")
        
        case "Qwen2VL_2B":
            list_Qwen2VL_2B = []
            model_Qwen2VL_2B, processor_Qwen2VL_2B = open_Qwen2VL_2B()
            for quality in videos_quality:
                for modification in videos_modifications:
                    for i, name in enumerate(os.listdir(os.path.join(args.input_frames,f"{quality}_{modification}"))):
                        path = os.path.join(args.input_frames,f"{quality}_{modification}", name)
                        list_Qwen2VL_2B.append(dict(video = f"{quality}_{modification}", frame_id = i+1, text = questionQwen2VL_2B(path, args.question, model_Qwen2VL_2B, processor_Qwen2VL_2B)))

            torch.cuda.empty_cache()   
            with open(os.path.join(args.result_output,"Qwen2VL_2B.json"), "w") as outfile:
                json.dump(list_Qwen2VL_2B, outfile)
            outfile.close()
            print("== Qwen2VL_2B SUCCESS ==")

        case _:
            print(f"Model {args.model} does not exit.")


if __name__ == "__main__":
    main()