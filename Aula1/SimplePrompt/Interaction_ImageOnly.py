import pathlib
import textwrap
import os
import google.generativeai as genai
import PIL.Image
from IPython.display import display
from IPython.display import Markdown

##############################################################################
#
#  Note
#  Establishing initial connection for a basic Image generative request.
#  Initial Python development phase
#
##############################################################################


def to_markdown(text):
  text = text.replace('•', '  *')
  return Markdown(textwrap.indent(text, '> ', predicate=lambda _: True))

# Get apy key from the enviroment
genai.configure(api_key=os.environ['API_KEY'])

model = genai.GenerativeModel('gemini-pro-vision')

img = PIL.Image.open(".\\Aula1\\img\\img1.png")

response = model.generate_content(img)
to_markdown(response.text)

print('Gemini: ": ',response.text)
print('response.prompt_feedback: ',response.prompt_feedback)
