import os
from groq import Groq
from flask import Flask, request, render_template_string, session

app = Flask(__name__)
app.secret_key = "clave_secreta_para_las_sesiones"  # Necesario para usar sesiones

# API key para el cliente Groq
API_KEY = "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"

# Página principal con un formulario simple para enviar mensajes
@app.route("/", methods=["GET", "POST"])
def chat():
    if "conversation" not in session:
        session["conversation"] = []  # Inicializa la conversación si no existe

    response = None
    if request.method == "POST":
        user_input = request.form["message"]

        # Agregar mensaje del usuario a la conversación
        session["conversation"].append({"role": "user", "content": user_input})

        # Obtener la respuesta del modelo Groq
        response = get_groq_response(session["conversation"])

        # Agregar la respuesta del modelo a la conversación
        session["conversation"].append({"role": "assistant", "content": response})
    
    # HTML simple con un formulario para ingresar el mensaje y mostrar la conversación
    html = """
    <h1>Chat con Groq</h1>
    <form method="POST">
        <label for="message">Escribe tu mensaje:</label><br>
        <input type="text" id="message" name="message" required><br><br>
        <input type="submit" value="Enviar">
    </form>
    <br>
    <h3>Historial de la conversación:</h3>
    <div>
        {% for msg in session.conversation %}
            <p><strong>{{ msg.role }}:</strong> {{ msg.content }}</p>
        {% endfor %}
    </div>
    """
    return render_template_string(html)

# Función para obtener la respuesta del modelo Groq
def get_groq_response(conversation):
    client = Groq(api_key=API_KEY)
    chat_completion = client.chat.completions.create(
        messages=conversation,  # Enviar todo el historial de la conversación
        model="llama3-8b-8192",
    )
    return chat_completion.choices[0].message.content


if __name__ == "__main__":
    app.run(debug=False, host='0.0.0.0')
