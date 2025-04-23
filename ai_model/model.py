from langchain_core.prompts import SystemMessagePromptTemplate, HumanMessagePromptTemplate, ChatPromptTemplate


class Model:
    """
    AI的模型对象 的父类
    """

    def create_llm(self):
        print('初始化大语言模型的对象')

    def make_prompt(self):
        """
        创建提示模板
        """
        system_template = """你是一个翻译专家，精通各种人类语言。\n
        输入的是：{source_language} 语言，翻译之后的语言为：{target_language}"""
        system_message_prompt = SystemMessagePromptTemplate.from_template(system_template)
        human_message_prompt = HumanMessagePromptTemplate.from_template('{text}')

        return ChatPromptTemplate.from_messages([system_message_prompt, human_message_prompt])
