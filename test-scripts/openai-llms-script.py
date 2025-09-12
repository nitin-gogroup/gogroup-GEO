import anthropic
from dotenv import load_dotenv
from llms_txt import create_ctx
import os
import requests

load_dotenv()

client = anthropic.Anthropic(api_key=os.getenv("ANTHROPIC_API_KEY"))
url = 'https://25139a722396.ngrok-free.app/llms.txt'
text = requests.get(url).text
llm_ctx = create_ctx(text)

conversation = [
    {"role": "user", "content": llm_ctx + '\n\nThe above is necessary context for the conversation.'},
    {"role": "user", "content": "Does GoGroup itself builds projects for clients? Or does it does that through partners or its organizations unit?"}
]

message = client.messages.create(
    model="claude-sonnet-4-20250514",
    max_tokens=1000,
    messages=conversation
)


print(message.content)