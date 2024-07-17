# 在 language_manager.py 中的 get_translation 函数

def get_translation(key, language=None):
    if language is None:
        language = language_manager.get_language()

    # 根据指定的语言返回对应的翻译，如果指定语言不存在则默认使用中文
    return translations.get(language, translations['zh']).get(key, translations['zh'].get(key, key))
