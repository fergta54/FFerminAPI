import os
from groq import Groq
from flask import Flask, request, render_template_string

app = Flask(__name__)

# API key para el cliente Groq
API_KEY = "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"

# Página principal con un formulario simple para enviar mensajes
@app.route("/", methods=["GET", "POST"])
def chat():
    response = None
    if request.method == "POST":
        user_input = request.form["message"]
        response = get_groq_response(user_input)
    
    # HTML simple con un formulario para ingresar el mensaje
    html = """
    <h1>Chat con Groq</h1>
    <form method="POST">
        <label for="message">Escribe tu mensaje:</label><br>
        <input type="text" id="message" name="message" required><br><br>
        <input type="submit" value="Enviar">
    </form>
    <br>
    {% if response %}
        <strong>Respuesta:</strong> {{ response }}
    {% endif %}
    """
    return render_template_string(html, response=response)

# Función para obtener la respuesta del modelo Groq
def get_groq_response(user_input):
    client = Groq(api_key=API_KEY)
    chat_completion = client.chat.completions.create(
        messages=[{"role": "user", "content": user_input}],
        model="llama3-8b-8192",
    )
    return chat_completion.choices[0].message.content


if __name__ == "__main__":
    app.run(debug=False, host='0.0.0.0')
