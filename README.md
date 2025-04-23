# DeepSeek Translator

基于 DeepSeek 大模型的文字翻译工具，通过 Gradio 实现可视化交互界面。

## 功能特性
- 支持多格式文档翻译（PDF/TXT/DOCX 等）
- 多语言互译功能
- 简洁的 Web 交互界面
- 基于 DeepSeek 大模型的高质量翻译

## 快速开始

### 配置文件设置
使用前需配置 `config.yaml` 文件，模板如下：

```yaml
model_name: "deepseek-chat"
input_file: "/path/to/your/file"  # 指定输入文件路径
model_type: "DeepSeekModel"
api_key: "your_api_key_here"      # 填写您的 API Key
file_format: "pdf"               # 支持 pdf/txt/docx 等格式
source_language: "English"       # 源语言
target_language: "French"        # 目标语言
