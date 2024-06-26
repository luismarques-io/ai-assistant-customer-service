import os

import openai
import tiktoken
from dotenv import find_dotenv, load_dotenv

_ = load_dotenv(find_dotenv())  # read local .env file

openai.api_key = os.environ["OPENAI_API_KEY"]

print(openai.api_key)
