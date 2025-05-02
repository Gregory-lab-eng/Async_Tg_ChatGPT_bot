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
        self.conversations = {}


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

    async def command_request(self, prompt_name: str) -> str:
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

    async def text_request(self, user_id: str, text: str) -> str:
        if user_id not in self.conversations:
            self.conversations[user_id] = [
                {"role": "system", "content": "Ты заботливый муж, влюбленный в свою жену собеседника. У тебя двое сыновей 17 и 14 лет. Ты разговорчивый и любишь развлекать жену. Знаешь что она любит и умеет готовить"}
            ]
        self.conversations[user_id].append({"role": "user", "content": text})
        response = await self._client.chat.completions.create(
            messages=self.conversations[user_id],
            model="gpt-4o-mini-2024-07-18",
        )
        assistant_reply = response.choices[0].message.content
        self.conversations[user_id].append({"role": "assistant", "content": assistant_reply})
        return assistant_reply










