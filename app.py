from llm_factory import get_llm

def main():
  print("🦋🦋🦋🦋Langchain LLM component demo. 🦋🦋🦋🦋")

  llm = get_llm()
  prompt = "Explain Langchain in simple terms. Even a 12 year old should understand"
  response = llm.invoke(prompt)
  print(f"Bot's response:: {response.content}")


if __name__ == "__main__":
  main()