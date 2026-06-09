# AI Assistant 🤖

Assistente virtual inteligente desenvolvido em Python, utilizando IA como copiloto no processo de criação e desenvolvimento do projeto.

## 💡 Sobre o Projeto

Este projeto explora o uso da Inteligência Artificial como um copiloto no desenvolvimento de software, auxiliando na criação de features de forma mais rápida e eficiente. A IA foi utilizada para sugerir soluções, gerar código, validar ideias e automatizar tarefas, permitindo foco em decisões estratégicas e criatividade.

## 🚀 Funcionalidades

- Conversa em linguagem natural em português
- Mantém histórico da conversa durante a sessão
- Respostas geradas por IA (LLaMA 3.3 70B via Groq)
- Interface simples via terminal

## 🛠️ Tecnologias Utilizadas

- Python 3
- [Groq API](https://console.groq.com)
- Modelo: LLaMA 3.3 70B Versatile
- GitHub Copilot (utilizado como copiloto durante o desenvolvimento)
- PyCharm

## ▶️ Como Executar

1. Clone o repositório:
   git clone https://github.com/seuusuario/AI-Assistant.git

2. Instale as dependências:
   pip install groq

3. Adicione sua chave da API Groq no arquivo main.py:
   client = Groq(api_key="SUA_CHAVE_AQUI")

4. Execute o projeto:
   python main.py

## 📌 Observação

Digite **sair** para encerrar a conversa.