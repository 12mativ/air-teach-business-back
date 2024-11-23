import os
from dotenv import load_dotenv
import autogen

load_dotenv()

config_list = {
  "config_list": [{
    "model": "gpt-3.5-turbo", 
    "api_key": os.getenv("OPENAI_API_KEY"),
  }]
}