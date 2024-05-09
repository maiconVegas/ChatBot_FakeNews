# -*- coding: utf-8 -*-
"""detector_FakeNews.ipynb

Instalando o SDK da google
"""

!pip install -q -U google-generativeai

import google.generativeai as genai

GOOGLE_API_KEY="SEU_API_KEY"
genai.configure(api_key=GOOGLE_API_KEY)

"""Listar os modelos disponíveis"""

for m in genai.list_models():
  if 'generateContent' in m.supported_generation_methods:
    print(m.name)

generation_config = {
    "candidate_count": 1,
    "temperature": 0.5,
}

safety_settings = {
    "HARASSMENT": "BLOCK_NONE",
    "HATE": "BLOCK_NONE",
    "SEXUAL": "BLOCK_NONE",
    "DANGEROUS": "BLOCK_NONE",
}

"""Inicializando o nosso modelo


"""

model = genai.GenerativeModel(model_name="gemini-1.0-pro",
                              generation_config=generation_config,
                              safety_settings=safety_settings)

"""função principal sobre funcionamento do programa"""

chat = model.start_chat(history=[])

# Solicitando entrada do usuário
prompt = input("Insira o texto do artigo ou o link: ")

# Verificando se é um link e obtendo o texto do artigo
if prompt.startswith("http"):

    text = prompt + " - [Insira um sim ou não sobre o link se é fake news ou não, analise o site e verifique se é fake news, elabore argumento e forneça links e forneça links se comprova ou não]"
else:
    text = prompt + " - [Insira um sim ou não sobre o argumento se é fake news ou não, elabore argumento e forneça links se comprova ou não]"

# Enviando o texto para o modelo
response = chat.send_message(text)

# Exibindo a resposta
print("Resposta do modelo:", response.text)