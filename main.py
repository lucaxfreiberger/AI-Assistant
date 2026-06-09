import os
from groq import Groq
from dotenv import load_dotenv

load_dotenv()

client = Groq(api_key=os.environ.get("GROQ_API_KEY"))


def assistant():
    print("Olá! Eu sou o AI Assistant. Digite 'sair' para encerrar.\n")

    historico = [
        {"role": "system",
         "content": "Você é um assistente virtual simpático e prestativo. Responda sempre em português."}
    ]

    while True:
        pergunta = input("Você: ")

        if pergunta.lower() == "sair":
            print("AI Assistant: Até mais!")
            break

        historico.append({"role": "user", "content": pergunta})

        resposta = client.chat.completions.create(
            model="llama-3.3-70b-versatile",
            messages=historico
        )

        texto = resposta.choices[0].message.content
        historico.append({"role": "assistant", "content": texto})

        print(f"AI Assistant: {texto}\n")


if __name__ == "__main__":
    assistant()