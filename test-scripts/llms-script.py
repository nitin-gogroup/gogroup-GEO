# requires-python = ">=3.8"
# dependencies = [
#     "claudette",
#     "llms-txt",
#     "requests",
# ]
# ///
from claudette import *
from llms_txt import create_ctx
from dotenv import load_dotenv

load_dotenv()

import requests

model = models[1] # Sonnet 4
print("model", model)
chat = Chat(model, sp="""You are a helpful and concise assistant.""")

url = 'https://25139a722396.ngrok-free.app/go-teams-llms.txt'
text = requests.get(url).text
llm_ctx = create_ctx(text)
chat(llm_ctx + '\n\nThe above is necessary context for the conversation.')

while True:
    print("\n\n-----------------QUESTION-------------------\n\n")
    msg = input('Your question about the site: ')
    res = chat(msg)
    print('From Claude:', contents(res))