from os import getenv, path
from dotenv import load_dotenv

from openai import AsyncOpenAI


class ChatGPT:
    _instance = None
    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            load_dotenv()
            cls._instance = super().__new__(cls)
        return cls._instance

    def __init__(self):
        self._OPENAI_API_KEY = getenv("OPENAI_API_KEY")
        self._client = self._create_client()


    def _create_client(self):
        gpt_client = AsyncOpenAI(
        api_key=self._OPENAI_API_KEY,
        )
        return gpt_client

    @staticmethod
    def _load_prompt(prompt_name: str) -> str:
        prompt_path = path.join('resources', 'prompts', f'{prompt_name}.txt')
        with open(prompt_path, 'r', encoding='UTF-8') as file:
            prompt = file.read()
        return prompt

    async def text_request(self, prompt_name: str) -> str:
        response = await self._client.chat.completions.create(
            messages=[
                {
                    'role': 'system',
                    'content': self._load_prompt(prompt_name),
                }
            ],
            model="gpt-4o-mini-2024-07-18",
        )
        return response.choices[0].message.content










