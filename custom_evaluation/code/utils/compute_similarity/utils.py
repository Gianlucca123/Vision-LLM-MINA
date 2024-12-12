import os

def display_scores(similarities):
    """
    @brief Displays similarity scores for given candidates.
    This function takes a dictionary of candidates and their corresponding similarity scores,
    and prints each candidate with its similarity score formatted to four decimal places.
    @param similarities A dictionary where keys are candidate names (str) and values are similarity scores (float).
    """

    for candidate, score in similarities.items():
        print(f"Similarity score for {candidate}: {score:.4f}")


def write_results(similarities, output_path):
    """
    @brief Writes the similarity scores to a file.
    This function takes a dictionary of candidates and their corresponding similarity scores,
    and writes them to a file in the format "candidate_name: similarity_score".
    @param similarities A dictionary where keys are candidate names (str) and values are similarity scores (float).
    @param output_path The path to the output file.
    """

    # Create a directory called "frames" if it does not already exist
    try:
        os.mkdir(output_path)
        print(f"Directory '{output_path}' created successfully.")
    except FileExistsError:
        print(f"Directory '{output_path}' already exists.")


    with open(os.path.join(output_path, "output.txt"), "w") as f:
        for candidate, score in similarities.items():
            f.write(f"{candidate}: {score:.4f}\n")