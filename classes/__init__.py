from .chatgpt import ChatGPT

gpt_client = ChatGPT()

__all__ = [
    'ChatGPT',
    'gpt_client',
]