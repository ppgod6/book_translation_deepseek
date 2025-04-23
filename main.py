from ai_model.deepseek_model import DeepSeekModel
from ai_model.openai_model import OpenAIModel
from translator.book_translator import PDFTranslator
from utils.project_config import ProjectConfig

if __name__ == '__main__':
    config = ProjectConfig()
    config.initialize()

    # 初始化大语言模型
    if config.model_type == 'DeepSeekModel':
        model = DeepSeekModel(config.model_name, config.api_key)
    else:
        model = OpenAIModel(config.model_name, config.api_key)
        pass

    # 初始化一个翻译器
    translator = PDFTranslator(model)
    translator.translate_book(file_path=config.input_file, source_language=config.source_language,
                              target_language=config.target_language, out_file_format=config.file_format)
