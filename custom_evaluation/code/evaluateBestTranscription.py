from utils.compute_similarity.sentence_transformer import compute_similarity_ST
from utils.compute_similarity.keyword_jaccard import compute_similarity_JKW
from utils.compute_similarity.utils import display_scores, write_results
import argparse


def main():
    parser = argparse.ArgumentParser(
        description="Evaluate the best transcription, given a ground truth and multiple candidate transcriptions."
    )
    parser.add_argument(
        "--ground_truth_path",
        type=str,
        required=True,
        default="../data/ground_truth/ground_truth.json",
        help="Path to the ground truth file.",
    )
    parser.add_argument(
        "--candidates_path_folder",
        type=str,
        required=True,
        default="../data/results_model",
        help="Path to the folder containing candidate files.",
    )
    parser.add_argument(
        "--ST_model_name",
        type=str,
        default="all-MiniLM-L6-v2",
        help="Name of the model to use for computing similarity with Sentence Transformer.",
    )
    parser.add_argument(
        "--write_results",
        action="store_true",
        help="Flag to write the results to a file.",
    )
    parser.add_argument(
        "--output",
        type=str,
        default="../data/benchmark_score",
        help="Name of the directory where the result is going to be stored.",
    )
    parser.add_argument(
        "--evaluation_mode",
        type=str,
        choices=["ST", "JKW"],
        required=True,
        help="Evaluation mode to use: 'ST' for Sentence Transformer or 'JKW' for Jaccard Keyword.",
    )
    parser.add_argument(
        "--text_file",
        action="store_true",
        help="Flag to indicate that the input files are text files. Default is JSON.",
    )

    args = parser.parse_args()

    if args.evaluation_mode == "ST":
        similarities = compute_similarity_ST(
            args.ground_truth_path,
            args.candidates_path_folder,
            model_name=args.ST_model_name,
            json_file=not args.text_file,
        )
    elif args.evaluation_mode == "JKW":
        similarities = compute_similarity_JKW(
            args.ground_truth_path,
            args.candidates_path_folder,
            json_file=not args.text_file,
        )

    display_scores(similarities)

    if args.write_results:
        write_results(similarities, args.output)


if __name__ == "__main__":
    main()

# e.g.
# python .\evaluateBestTranscription.py --ground_truth_path "data/input/ground_truth/flying_whales.txt" --candidates_path_folder "data/output/transcription" --write_results --output_path "data/output/benchmark/output_ST.txt" --evaluation_mode "ST"
