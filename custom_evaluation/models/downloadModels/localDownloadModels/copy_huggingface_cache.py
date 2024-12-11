import argparse
import shutil
import os

def copy_huggingface_cache(source_dir, destination_dir):
    # Expand the user directory for the source path
    source_dir = os.path.expanduser(source_dir)

    # Ensure the source directory exists
    if not os.path.exists(source_dir):
        print(f"Source directory {source_dir} does not exist.")
        return

    # Ensure the destination directory exists
    if not os.path.exists(destination_dir):
        os.makedirs(destination_dir)

    # Copy the entire directory
    try:
        shutil.copytree(source_dir, os.path.join(destination_dir, 'huggingface'), dirs_exist_ok=True)
        print(f"Successfully copied {source_dir} to {destination_dir}")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Copy Hugging Face cache directory.")
    parser.add_argument("source_dir", type=str, help="Source directory to copy from. For example: ~/.cache/huggingface or /home/bob/Desktop/huggingface")
    parser.add_argument("destination_dir", type=str, help="Destination directory to copy to. For example: /home/bob/Desktop or ~/.cache")

    args = parser.parse_args()

    copy_huggingface_cache(args.source_dir, args.destination_dir)
