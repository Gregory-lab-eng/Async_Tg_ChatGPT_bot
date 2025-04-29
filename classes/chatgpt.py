from os import getenv
from dotenv import load_dotenv

from openai import OpenAI

load_dotenv()

OPENAI_API_KEY = getenv("OPENAI_API_KEY")

client = OpenAI()

response = client.responses.create(
        model="gpt-4o-mini-2024-07-18",
        input="факт про язык питон",
        instructions="дай любой рандомный факт"
    )
print(response.output_text)