from sentence_transformers import SentenceTransformer, util
from pathlib import Path


def load_model(model_name: str = "all-MiniLM-L6-v2"):
    """
    @brief Loads a SentenceTransformer model.
    @param model_name The name of the model to load. Default is 'all-MiniLM-L6-v2'.
    @return The loaded SentenceTransformer model.
    """
    model = SentenceTransformer(model_name)
    return model


def split_text(text, max_length=100):
    """
    Splits a given text into chunks of a specified maximum length.
    @param text: The input text to be split.
    @type text: str
    @param max_length: The maximum number of words in each chunk. Default is 100.
    @type max_length: int
    @return: A list of text chunks, each containing up to max_length words.
    @rtype: list of str
    """

    words = text.split()
    return [
        " ".join(words[i : i + max_length]) for i in range(0, len(words), max_length)
    ]


def get_document_embedding(model, text, max_length=100):
    """
    Computes the embedding for a given document using a specified model.
    This function splits the input text into segments of a specified maximum length,
    encodes each segment using the provided model, and then computes the mean of the
    embeddings to obtain a single embedding for the entire document.
    @param model: The model used to encode the text segments.
    @type model: SentenceTransformer or similar model with an encode method.
    @param text: The input document text to be embedded.
    @type text: str
    @param max_length: The maximum length of each text segment. Default is 100.
    @type max_length: int
    @return: The embedding for the entire document.
    @rtype: torch.Tensor
    """

    segments = split_text(text, max_length=max_length)
    embeddings = model.encode(segments, convert_to_tensor=True)

    # Compute the mean of the embeddings to get a single embedding for the entire document
    document_embedding = embeddings.mean(dim=0)
    return document_embedding


def compute_similarity_ST(
    ground_truth_path, candidates_path_folder, model_name="all-MiniLM-L6-v2"
):
    """
    Compute the similarity (cosine similarity) between a ground truth document and multiple candidate documents using a specified sentence transformer model.
    @param ground_truth_path: Path to the ground truth document.
    @type ground_truth_path: str
    @param candidates_path_folder: Path to the folder containing candidate documents.
    @type candidates_path_folder: str
    @param model_name: Name of the sentence transformer model to use. Default is 'all-MiniLM-L6-v2'.
    @type model_name: str
    @return: A dictionary where keys are candidate document names (without extension) and values are their similarity scores to the ground truth document.
    @rtype: dict
    """

    # Load the sentence transformer model
    model = load_model(model_name)

    # Load the ground truth document
    ground_truth_path = Path(ground_truth_path)
    ground_truth = ground_truth_path.read_text(encoding="utf-8")

    # Compute the embedding for the ground truth document
    gt_embedding = get_document_embedding(model, ground_truth)

    # Compute the similarity between the ground truth document and each candidate document
    similarities = {}
    candidates_folder_path = Path(candidates_path_folder)
    candidates_paths = list(candidates_folder_path.glob("*.txt"))

    for candidate_path in candidates_paths:
        candidate = candidate_path.read_text(encoding="utf-8")
        candidate_embedding = get_document_embedding(model, candidate)
        similarity = util.cos_sim(
            gt_embedding, candidate_embedding
        ).item()  # Cosine similarity
        similarities[candidate_path.stem] = similarity

    return similarities