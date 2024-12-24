import json

def get_answer(question, file_path="data.json"):
    with open(file_path, "r", encoding="utf-8") as file:
        data = json.load(file)
    return data.get(question, "Извините, я не нашел ответа на этот вопрос. Попробуйте переформулировать запрос.")
