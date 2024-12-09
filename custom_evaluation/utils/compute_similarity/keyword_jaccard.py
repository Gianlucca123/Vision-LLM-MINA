import nltk
from pathlib import Path
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer
from collections import Counter

# Ensure you have the necessary NLTK data files
# nltk.download('punkt')
# nltk.download('stopwords')
# nltk.download('wordnet')
# nltk.download('punkt_tab')


def extract_lemmas(text):
    """
    Extracts lemmas from a given text using NLTK.
    @param text: The input text from which lemmas are to be extracted.
    @type text: str
    @return: A list of lemmas extracted from the input text.
    @rtype: list of str
    """
    lemmatizer = WordNetLemmatizer()
    stop_words = set(stopwords.words("english"))
    tokens = word_tokenize(text)
    lemmas = [
        lemmatizer.lemmatize(token.lower())
        for token in tokens
        if token.isalnum() and token.lower() not in stop_words
    ]
    return lemmas


def compute_similarity_JKW(ground_truth_path, candidates_path_folder):
    """
    Compute the Jaccard similarity between a ground truth document and multiple candidate documents using NLTK.
    @param ground_truth_path: Path to the ground truth document.
    @param candidates_path_folder: Path to the folder containing candidate documents.
    @return: A dictionary containing Jaccard similarity scores for each candidate document.
    @rtype: dict
    """
    ground_truth_text = Path(ground_truth_path).read_text(encoding="utf8")
    ground_truth_lemmas = Counter(extract_lemmas(ground_truth_text))

    similarities = {}

    for candidate_path in Path(candidates_path_folder).glob("*.txt"):
        candidate_text = candidate_path.read_text(encoding="utf8")
        candidate_lemmas = Counter(extract_lemmas(candidate_text))

        intersection = sum((ground_truth_lemmas & candidate_lemmas).values())
        union = sum((ground_truth_lemmas | candidate_lemmas).values())
        jaccard_similarity = intersection / union
        similarities[candidate_path.stem] = jaccard_similarity

    return similarities
