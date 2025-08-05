import os
from openai import OpenAI
from dotenv import load_dotenv

# Load your .env file with the API key
load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")

# Initialize the OpenAI client
client = OpenAI(api_key=api_key)

def summarize_diff(diff_text):
    prompt = f"""You're a helpful assistant. Summarize the key changes between two document versions shown below:\n\n{diff_text}\n\nSummary:"""

    response = client.chat.completions.create(
        model="gpt-4",
        messages=[
            {"role": "user", "content": prompt}
        ],
        temperature=0.3,
        max_tokens=500
    )

    return response.choices[0].message.content.strip()
