import os
from collections import defaultdict

def display_scores(similarities):
    """
    @brief Displays similarity scores for given candidates.
    This function takes a dictionary of candidates and their corresponding similarity scores,
    and prints each candidate with its similarity score formatted to four decimal places.
    @param similarities A dictionary where keys are candidate names (str) and values are similarity scores (float).
    """

    for candidate, (score, mean_time) in similarities.items():
        print(f"Similarity score for {candidate}: {score:.4f}  {mean_time:.2f}s")


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


    # Step 1: Group models by resolution and modification
    grouped_models = defaultdict(dict)
    for candidate, (score, mean_time) in similarities.items():
        # Split the model name into parts
        parts = candidate.split('_')
        # Extract resolution and modification
        if(parts[0] in ["InternVL2","Qwen2VL"]):
            resolution_modification =' '.join(parts[2:])
            model_name = parts[0] + "_" + parts[1]
        else:
            resolution_modification = ' '.join(parts[1:])
            model_name = parts[0]
        
        # Group by resolution and modification
        grouped_models[resolution_modification][model_name] = (score, mean_time)

    # Step 2: Write the grouped information to the file
    with open(os.path.join(output_path, "output.txt"), "w") as f:
        for res_mod, models in grouped_models.items():
            f.write(f"{res_mod}:\n")
            best_model = max(models, key=lambda k: models[k][0])
            for model_name, (score, mean_time) in models.items():
                indicator = " <-- best score" if model_name == best_model else ""
                f.write(f"       {model_name}: {score:.4f}     {mean_time:.2f}s{indicator}\n")