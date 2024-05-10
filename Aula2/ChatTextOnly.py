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

#set model
model = genai.GenerativeModel('gemini-1.5-pro-latest')

#start chat model with no history
chat = model.start_chat(history=[])

my_text = "x"
while my_text != '':
 
    if my_text != '' and my_text != 'x' :
        
        prompt_parts = [
        "Input: "+my_text,
        "output: 1 - Craft a response that playfully pokes fun at my previous statement as you were a infinitly old wizard. 2 - Your name is Salabim. 3 - Try to end your sentence introducing another interesting topic to talk about."
        ]

        response = chat.send_message(prompt_parts)
        to_markdown(response.text)
        print("Gemini: ",response.text)
        print(response.prompt_feedback)

    my_text = input("New input: ")
