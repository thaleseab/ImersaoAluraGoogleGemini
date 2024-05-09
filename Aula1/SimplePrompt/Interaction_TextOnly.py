import pathlib
import textwrap
import os
import google.generativeai as genai
from IPython.display import display
from IPython.display import Markdown


##############################################################################
#
#  Note
#  Establishing initial connection for a basic text generative request.
#  Initial Python development phase
#
##############################################################################


def to_markdown(text):
  text = text.replace('•', '  *')
  return Markdown(textwrap.indent(text, '> ', predicate=lambda _: True))

# Get apy key from the enviroment
genai.configure(api_key=os.environ['API_KEY'])

model = genai.GenerativeModel('gemini-pro')

my_text =  "What is the meaning of life?"

response = model.generate_content(my_text)
to_markdown(response.text)

print("Gemini: ",response.text)
print('response.prompt_feedback: ',response.prompt_feedback)

