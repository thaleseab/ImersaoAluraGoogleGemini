######################################################################################################### 
# 
# Projeto: Be my eye
#
# Análise de conteúdo visual e emocional em imagem, video e audio. 
#
# Embora útil no dia a dia, o foco está em descrever detalhadamente 
# ambientes em situações de risco para pessoas com deficiencia visual em momento crítico. 
#
# Movido pelo Google Gemini:
# Detecta emoções, identifica elementos com clareza. 
# Prove localizaçäo geograficamente e temporal. 
# Descreve objetos e condições de luz. 
# Segrega cenas distintas.
# Infere riscos a saúde / vida.
# 
########################################################################################################

import pathlib
import textwrap
import os
import google.generativeai as genai
import PIL.Image
from IPython.display import display
from IPython.display import Markdown

def to_markdown(text):
  text = text.replace('•', '  *')
  return Markdown(textwrap.indent(text, '> ', predicate=lambda _: True))

genai.configure(api_key=os.environ['API_KEY'])

# Set up the model
generation_config = {
  "temperature": 1,
  "top_p": 0.95,
  "top_k": 0,
  "max_output_tokens": 8192,
}

safety_settings = [
  {
    "category": "HARM_CATEGORY_HARASSMENT",
    "threshold": "BLOCK_NONE"
  },
  {
    "category": "HARM_CATEGORY_HATE_SPEECH",
    "threshold": "BLOCK_NONE"
  },
  {
    "category": "HARM_CATEGORY_SEXUALLY_EXPLICIT",
    "threshold": "BLOCK_NONE"
  },
  {
    "category": "HARM_CATEGORY_DANGEROUS_CONTENT",
    "threshold": "BLOCK_NONE"
  },
]

system_instruction = "Descreva usando as seguintes regras:\nAnalise minuciosamente o conteúdo, identificando e descrevendo as emoções ou sentimentos expressos por pessoas ou animais, contribuindo para a compreensão do contexto emocional da cena.\nDescreva de forma definitiva o que foi identificado com certeza absoluta.\nEm caso de incerteza na identificação de algo, mencione essa dúvida. Nunca descreva algo incerto sem indicar a incerteza.\nIndique a localização geográfica de onde o conteúdo foi produzido, especificando se é uma certeza ou uma possibilidade.\nEspecifique a época retratada no conteúdo, indicando se é uma certeza ou uma possibilidade.\nInclua informações sobre a disposição espacial dos objetos na cena.\nDescreva a hora do dia e/ou a luminosidade presente na cena.\nSe o conteúdo apresentar cenas distintas, tente descrevê-las separadamente.\nIdentifique possíveis e/ou iminentes perigos."

model = genai.GenerativeModel(model_name="gemini-1.5-pro-latest",
                              generation_config=generation_config,
                              system_instruction=system_instruction,
                              safety_settings=safety_settings)

convo = model.start_chat(history=[])

for i in range(1, 12):
  img = PIL.Image.open(".\\img\\img"+str(i)+".png")
  response = model.generate_content(img)
  to_markdown(response.text)
  print('Gemini response to img'+str(i)+'.png:\n\n',response.text,"\n\n\n\n--------------------------------------\n\n")
