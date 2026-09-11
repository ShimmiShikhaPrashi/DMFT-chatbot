import os
from dotenv import load_dotenv
from google import genai

from document_search import search_documents

load_dotenv()

client = genai.Client(
    api_key=os.getenv("GEMINI_API_KEY")
)


def get_ai_response(question):

    try:

        relevant_information = search_documents(question)

        prompt = f"""
You are the DMFT Assistant.

Answer ONLY using the official document information provided below.

If the information is not available in the documents, clearly say:

"This information is not available in the currently uploaded official documents."

Answer in the same language as the user's question.

OFFICIAL INFORMATION:

{relevant_information}

QUESTION:

{question}
"""

        interaction = client.interactions.create(
            model="gemini-3.6-flash",
            input=prompt
        )

        return interaction.output_text

    except Exception as error:

        print("GEMINI ERROR:", error)

        return f"Error connecting to AI: {error}"