from models.callModels.InternVL2_1B import questionInternVL2_1B, open_InternVL2_1B
from models.callModels.Kosmos2 import questionKosmos2, open_Kosmos2
from models.callModels.MiniCPMV2 import questionMiniCPMV2, open_MiniCPMV2
from models.callModels.Mississippi import questionMississippi, open_Mississippi
from models.callModels.Moondream2 import questionMoondream2, open_Moondream2
from models.callModels.Qwen2VL_2B import questionQwen2VL_2B, open_Qwen2VL_2B
from models.callModels.DeepSeek13BVL import questionDeepSeek13BVL, open_DeepSeek13BVL
import json
from PIL import Image
import torch
import argparse
import os
import time

def main():    
    parser = argparse.ArgumentParser(
        description="Generate a Json file with the result of the model specified"
    )

    parser.add_argument(
        "--model",
        type=str,
        default="Moondream2",
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
        default="data/frames",
        help="Path to the frames.",
    )

    parser.add_argument(
        "--result_output",
        type=str,
        default="data/results_model",
        help="Name of the directory where the results are going to be stored.",
    )

    parser.add_argument(
        "--video_quality",
        nargs='+',
        choices=["1080p", "720p", "480p", "240p"],
        default=["1080p"],
        help="Define quality of the videos"
    )

    parser.add_argument(
        "--video_modifications",
        nargs='+',
        choices=[
        "no_modification",
        "blur",
        "noise",
        "black_and_white",
        "distortion",
        "different_color_space"
        ],
        default=["no_modification"],
        help="modifications for the video"
    )

    args = parser.parse_args()

    # Create a directory to store the results, if it does not already exist.
    try:
        os.mkdir(args.result_output)
        print(f"Directory '{args.result_output}' created successfully.")
    except FileExistsError:
        print(f"Directory '{args.result_output}' already exists.")


    match args.model:
        case "Moondream2":
            list_Moondream2 = []
            model_Moondream2, tokenizer_Moondream2 = open_Moondream2()
            for quality in args.video_quality:
                for modification in args.video_modifications:
                    for i, name in enumerate(os.listdir(os.path.join(args.input_frames,f"{quality}_{modification}"))):
                        path = os.path.join(args.input_frames,f"{quality}_{modification}", name)
                        image = Image.open(path)
                        start_timer = time.time()
                        answer = questionMoondream2(args.question, model_Moondream2, tokenizer_Moondream2, image) 
                        end_timer = time.time()
                        time_inf = end_timer - start_timer
                        list_Moondream2.append(dict(frame_id = i+1, text = answer, inference_time=time_inf)) 
                        print(f"question asked for frame {i+1} of video {quality}_{modification}")
                        
                    with open(os.path.join(args.result_output,f"{args.model}_{quality}_{modification}.json"), "w") as outfile:
                        json.dump(list_Moondream2, outfile)
                    outfile.close()
                    list_Moondream2.clear()

            torch.cuda.empty_cache()
            print("== Moondream2 SUCCESS ==")

        case "InternVL2_1B":
            list_InternVL2_1B = []
            model_InternVL2, tokenizer_InternVL2 = open_InternVL2_1B()
            for quality in args.video_quality:
                for modification in args.video_modifications:
                    for i, name in enumerate(os.listdir(os.path.join(args.input_frames,f"{quality}_{modification}"))):
                        path = os.path.join(args.input_frames,f"{quality}_{modification}", name)
                        image_rgb = Image.open(path).convert('RGB')
                        start_timer = time.time()
                        answer = questionInternVL2_1B(args.question, model_InternVL2, tokenizer_InternVL2, image_rgb)
                        end_timer = time.time()
                        time_inf = end_timer - start_timer
                        list_InternVL2_1B.append(dict(frame_id = i+1, text = answer, inference_time=time_inf))
                        print(f"question asked for frame {i+1} of video {quality}_{modification}")
            
                    with open(os.path.join(args.result_output,f"{args.model}_{quality}_{modification}.json"), "w") as outfile:
                        json.dump(list_InternVL2_1B, outfile)
                    outfile.close()
                    list_InternVL2_1B.clear()

            torch.cuda.empty_cache()
            print("== InternVL2_1B SUCCESS ==")

        case "Kosmos2":
            list_Kosmos2 = []
            model_Kosmos2, processor_Komos2, device_Kosmos2 = open_Kosmos2()
            for quality in args.video_quality:
                for modification in args.video_modifications:
                    for i, name in enumerate(os.listdir(os.path.join(args.input_frames,f"{quality}_{modification}"))):
                        path = os.path.join(args.input_frames,f"{quality}_{modification}", name)
                        image = Image.open(path)
                        start_timer = time.time()
                        answer = questionKosmos2(args.question, model_Kosmos2, processor_Komos2, device_Kosmos2, image)
                        end_timer = time.time()
                        time_inf = end_timer  - start_timer
                        list_Kosmos2.append(dict(frame_id = i+1, text = answer, inference_time = time_inf))
                        print(f"question asked for frame {i+1} of video {quality}_{modification}")
            
                    with open(os.path.join(args.result_output,f"{args.model}_{quality}_{modification}.json"), "w") as outfile:
                        json.dump(list_Kosmos2, outfile)
                    outfile.close()
                    list_Kosmos2.clear()

            torch.cuda.empty_cache()
            print("== Kosmos2 SUCCESS ==")

        case "MiniCPMV2":
            list_MiniCPMV2 = []
            model_MiniCPMV2, tokenizer_MiniCPMV2 = open_MiniCPMV2()
            for quality in args.video_quality:
                for modification in args.video_modifications:
                    for i, name in enumerate(os.listdir(os.path.join(args.input_frames,f"{quality}_{modification}"))):
                        path = os.path.join(args.input_frames,f"{quality}_{modification}", name)
                        image_rgb = Image.open(path).convert('RGB')
                        start_timer = time.time()
                        answer = questionMiniCPMV2(args.question, model_MiniCPMV2, tokenizer_MiniCPMV2, image_rgb)
                        end_timer = time.time()
                        time_inf = end_timer - start_timer 
                        list_MiniCPMV2.append(dict(frame_id = i+1, text = answer, inference_time = time_inf))
                        print(f"question asked for frame {i+1} of video {quality}_{modification}")
                       
                    with open(os.path.join(args.result_output,f"{args.model}_{quality}_{modification}.json"), "w") as outfile:
                        json.dump(list_MiniCPMV2, outfile)
                    outfile.close()
                    list_MiniCPMV2.clear()

            torch.cuda.empty_cache()
            print("== MiniCPMV2 SUCCESS ==")

        case "Mississippi":
            list_Mississippi = []
            model_Mississippi, tokenizer_Mississippi, generation_config_Mississippi = open_Mississippi()
            for quality in args.video_quality:
                for modification in args.video_modifications:
                    for i, name in enumerate(os.listdir(os.path.join(args.input_frames,f"{quality}_{modification}"))):
                        path = os.path.join(args.input_frames,f"{quality}_{modification}", name)
                        start_timer = time.time()
                        answer = questionMississippi(path, args.question, model_Mississippi, tokenizer_Mississippi, generation_config_Mississippi)
                        end_timer = time.time()
                        time_inf = end_timer - start_timer
                        list_Mississippi.append(dict(frame_id = i+1, text = answer, inference_time = time_inf))
                        print(f"question asked for frame {i+1} of video {quality}_{modification}")
             
                    with open(os.path.join(args.result_output,f"{args.model}_{quality}_{modification}.json"), "w") as outfile:
                        json.dump(list_Mississippi, outfile)
                    outfile.close()
                    list_Mississippi.clear()

            torch.cuda.empty_cache()
            print("== Mississippi SUCCESS ==")
        
        case "Qwen2VL_2B":
            list_Qwen2VL_2B = []
            model_Qwen2VL_2B, processor_Qwen2VL_2B = open_Qwen2VL_2B()
            for quality in args.video_quality:
                for modification in args.video_modifications:
                    for i, name in enumerate(os.listdir(os.path.join(args.input_frames,f"{quality}_{modification}"))):
                        path = os.path.join(args.input_frames,f"{quality}_{modification}", name)
                        start_timer = time.time()
                        answer = questionQwen2VL_2B(path, args.question, model_Qwen2VL_2B, processor_Qwen2VL_2B)
                        end_timer = time.time()
                        time_inf = end_timer - start_timer
                        list_Qwen2VL_2B.append(dict(frame_id = i+1, text = answer, inference_time = time_inf))
                        print(f"question asked for frame {i+1} of video {quality}_{modification}")
               
                    with open(os.path.join(args.result_output,f"{args.model}_{quality}_{modification}.json"), "w") as outfile:
                        json.dump(list_Qwen2VL_2B, outfile)
                    outfile.close()
                    list_Qwen2VL_2B.clear()

            torch.cuda.empty_cache()
            print("== Qwen2VL_2B SUCCESS ==")
        
        case "DeepSeek-1.3B-VL":
            list_DeepSeek13BVL = []
            vl_chat_processor,tokenizer,vl_gpt = open_DeepSeek13BVL()
            for quality in args.video_quality:
                for modification in args.video_modifications:
                    for i, name in enumerate(os.listdir(os.path.join(args.input_frames,f"{quality}_{modification}"))):
                        image_path = os.path.join(args.input_frames,f"{quality}_{modification}", name)
                        start_timer = time.time()
                        answer = questionDeepSeek13BVL(args.question, vl_chat_processor, tokenizer, vl_gpt, image_path)
                        end_timer = time.time()
                        time_inf = end_timer - start_timer
                        list_DeepSeek13BVL.append(dict(frame_id = i+1, text = answer, inference_time = time_inf))
                        print(f"question asked for frame {i+1} of video {quality}_{modification}")
             
                    with open(os.path.join(args.result_output,f"{args.model}_{quality}_{modification}.json"), "w") as outfile:
                        json.dump(list_DeepSeek13BVL, outfile)
                    outfile.close()
                    list_DeepSeek13BVL.clear()

            torch.cuda.empty_cache()
            print("== DeepSeek-1.3B-VL SUCCESS ==")

        case _:
            print(f"Model {args.model} does not exit.")


if __name__ == "__main__":
    main()