# generate_language_manager_script.py

translations = {
    'zh': {
        'welcome_message': "您好！以下是可用的命令：\n"
                           "/language - 切换语言 (Switch language)\n"
                           "/start - 再次发送此帮助消息（输入非命令字符也可推送帮助）\n"
                           # 省略其他翻译信息...
                           "/uploadkeys - 批量上传公钥到远程主机",
        # 省略其他翻译信息...
    },
    'en': {
        'welcome_message': "Hello! Here are the available commands:\n"
                           "/language - Switch language (切换语言)\n"
                           "/start - Send this help message again (non-command input will also trigger help)\n"
                           # 省略其他翻译信息...
                           "/uploadkeys - Batch upload public keys to remote hosts",
        # 省略其他翻译信息...
    }
}

def generate_language_manager_script(translations):
    with open('language_manager.py', 'r', encoding='utf-8') as file:
        content = file.read()

    updated_content = content.split('translations = {')[0]  # 截取到 translations 前的内容

    updated_content += 'translations = {\n'
    for lang, translation_dict in translations.items():
        updated_content += f"    '{lang}': {{\n"
        for key, value in translation_dict.items():
            updated_content += f"        '{key}': \"{value}\",\n"
        updated_content += "    },\n"
    updated_content += "}\n\n"

    with open('language_manager.py', 'w', encoding='utf-8') as file:
        file.write(updated_content)

    print("Successfully generated script to update language_manager.py!")

# 生成脚本并更新 language_manager.py
generate_language_manager_script(translations)
