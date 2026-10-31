import os
import json
from dotenv import load_dotenv

from langchain_openai import ChatOpenAI
from langchain_google_genai import ChatGoogleGenerativeAI

load_dotenv()

with open("config.json", "r") as f:
  config = json.load(f)

provider = config["provider"]

## Initialize the LLM

if provider=="openai":
  llm = ChatOpenAI(
      model=config["openai"]["model"],
      temperature=config["openai"]["temperature"],
      max_tokens=config["openai"]["max_tokens"],
      api_key=os.getenv("OPENAI_API_KEY")
  )
elif provider=="gemini":
  llm = ChatGoogleGenerativeAI(
      model=config["gemini"]["model"],
      temperature=config["gemini"]["temperature"],
      max_tokens=config["gemini"]["max_tokens"],
      api_key=os.getenv("GEMINI_API_KEY")
  )
else:
  raise ValueError("Invalid provider. It should be openai or gemini")

prompt = "What is thr capital of Japan ?"
print(f"\n Using provider {provider.capitalize()}, ({type(llm).__name__})")

response = llm.invoke(prompt)

print(f"Bot's response:: {response}")

