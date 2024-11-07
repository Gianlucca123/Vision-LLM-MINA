from custom_evaluation import custom_evaluation
import argparse


def main():
    parser = argparse.ArgumentParser(
        description="Run custom evaluation on a specific video."
    )
    parser.add_argument("video_path", type=str, help="Path to the video file.")
    parser.add_argument(
        "ground_truth_path", type=str, help="Path to the ground truth file."
    )
    parser.add_argument("model_path", type=str, help="Path to the model file.")
    parser.add_argument(
        "video_model",
        type=bool,
        help="Boolean to indicate if the model takes the whole video as input (True means yes).",
    )
    parser.add_argument(
        "fps",
        type=int,
        help="Maximum frames per second to process. (if no limit set it to 0)",
    )

    args = parser.parse_args()
    custom_evaluation(args.video_path)


if __name__ == "__main__":
    main()
