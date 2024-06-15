import os
from groq import Groq
from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route("/")
def root():
    return "root"


@app.route("/datosMes")
def mes():
    client = Groq(
    api_key="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",
    )
    chat_completion = client.chat.completions.create(
        messages=[
            {
                "role": "user",
                "content": "Escribe solamente un numero del 1 al 10 nada mas",
            }
        ],
        model="llama3-8b-8192",
    )
    res = chat_completion.choices[0].message.content
    return res

@app.route("/datosSem")
def mes():
    client = Groq(
    api_key="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",
    )
    chat_completion = client.chat.completions.create(
        messages=[
            {
                "role": "user",
                "content": "Solo dame un ejemplo de una tabla de my sql nada mas gracias.",
            }
        ],
        model="llama3-8b-8192",
    )
    res = chat_completion.choices[0].message.content
    return res



if __name__ == "__main__":
    app.run(debug=False,host='0.0.0.0')
