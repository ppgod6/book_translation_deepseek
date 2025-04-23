from langchain_deepseek import ChatDeepSeek

from ai_model.model import Model


class DeepSeekModel(Model):

    def __init__(self, model_name: str, api_key: str):
        self.model_name = model_name
        self.api_key = api_key

    def create_llm(self):
        return ChatDeepSeek(model=self.model_name, api_key=self.api_key, temperature=0)
