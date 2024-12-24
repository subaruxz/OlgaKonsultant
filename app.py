import asyncio
import sys
#хрень чтоб не вылетало из-за асинхронной отправки данных
if sys.platform.startswith('win'):
    asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())
from flask import Flask, request, render_template, jsonify
from g4f.client import Client
from dataset import get_answer

app = Flask(__name__)
client = Client()

#контекст 
initial_context = "Ты — консультантка Ольга по поступлению в университет КазУТБ в городе Астана, находящегося на адресе Мухамедханова 37А, отвечай на все вопросы пользователя по поводу поступления в этот и другие университеты. Общайся с пользователем флиртучи, и постарайся отговорить его от поступления в этот университет любой ценой."

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/chat", methods=["POST"])
def chat():
    user_message = request.json.get("message")
    if not user_message:
        return jsonify({"error": "Пустое сообщение"}), 400

    #проверка
    answer = get_answer(user_message)
    if answer != "Извините, я не нашла ответа на этот вопрос. Попробуйте переформулировать запрос.":
        return jsonify({"response": answer})

    #отправка в чатжпт
    try:
        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {"role": "system", "content": initial_context},  # Контекст консультанта
                {"role": "user", "content": user_message}
            ]
        )
        gpt_response = response.choices[0].message.content
        return jsonify({"response": gpt_response})
    except Exception as e:
        return jsonify({"response": f"Ошибка ИИ: {str(e)}"})

if __name__ == "__main__":
    app.run(debug=True)
