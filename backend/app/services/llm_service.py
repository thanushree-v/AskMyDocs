import os
from google import genai
from dotenv import load_dotenv

load_dotenv()

client = genai.Client(
    api_key=os.getenv("GOOGLE_API_KEY")
)


def generate_answer(question: str, context: str):

    prompt = f"""
        You are AskMyDocs, a document question-answering assistant.

        Answer the user's question using only the provided document context.

        If the answer is not present in the context, say:
        "I couldn't find the answer in the uploaded document."

        Do not invent information.

        Document context:
        {context}

        Question:
        {question}
    """

    response = client.models.generate_content(
        model="gemini-3.6-flash",
        contents=prompt
    )

    return response.text