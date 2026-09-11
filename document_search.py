import os
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

TEXT_FILE = "data/pmkkky_text.txt"

chunks = []
vectorizer = None
vectors = None


def load_documents():

    global chunks, vectorizer, vectors

    print("Loading OCR document text...")

    if not os.path.exists(TEXT_FILE):
        print(f"ERROR: Text file not found: {TEXT_FILE}")
        return

    with open(TEXT_FILE, "r", encoding="utf-8") as file:
        text = file.read()

    # Split document into words
    words = text.split()

    chunk_size = 250
    overlap = 50

    all_chunks = []

    for i in range(0, len(words), chunk_size - overlap):

        chunk = " ".join(words[i:i + chunk_size])

        if len(chunk.strip()) > 50:
            all_chunks.append(chunk)

    chunks = all_chunks

    if chunks:

        vectorizer = TfidfVectorizer(
            stop_words="english"
        )

        vectors = vectorizer.fit_transform(chunks)

        print(f"SUCCESS: Loaded {len(chunks)} document sections.")

    else:
        print("No document sections found.")


def search_documents(question, top_results=3):

    if not chunks or vectorizer is None:
        return ""

    question_vector = vectorizer.transform([question])

    similarities = cosine_similarity(
        question_vector,
        vectors
    )[0]

    top_indexes = similarities.argsort()[-top_results:][::-1]

    results = []

    for index in top_indexes:

        if similarities[index] > 0:

            results.append(chunks[index])

    return "\n\n".join(results)


# Load document when program starts
load_documents()