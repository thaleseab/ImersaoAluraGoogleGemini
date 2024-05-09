import pathlib
import textwrap
import os
import google.generativeai as genai
from IPython.display import display
from IPython.display import Markdown

##################################################################
#
#  Note
#  Establishing initial connection for a basic generative request.
#  Initial Python development phase
#
##################################################################


def to_markdown(text):
  text = text.replace('•', '  *')
  return Markdown(textwrap.indent(text, '> ', predicate=lambda _: True))

genai.configure(api_key=os.environ['API_KEY'])

model = genai.GenerativeModel('gemini-pro')

response = model.generate_content("What is the meaning of life?")
to_markdown(response.text)

print(response.text)
print(response.prompt_feedback)
