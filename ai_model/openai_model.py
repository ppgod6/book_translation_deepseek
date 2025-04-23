from langchain_openai import ChatOpenAI

from ai_model.model import Model


class OpenAIModel(Model):

    def __init__(self, model_name: str, api_key: str):
        self.model_name = model_name
        self.api_key = api_key

    def create_llm(self):
        """
        初始化openai的大语言模型对象
        :return:
        """
        return ChatOpenAI(model=self.model_name, api_key=self.api_key, temperature=0.5)
