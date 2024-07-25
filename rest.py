import requests
import os

url = "https://api.groq.com/openai/v1/chat/completions"
headers = {"Authorization": "Bearer " + str(os.environ.get("GROQ_API_KEY"))}
query = "Which nummber is bigger: 9.11 or 9.9?"
data = {"messages": [{"role": "user", "content": query}], "model": "llama-3.1-70b-versatile"}

response = requests.post(url, headers=headers, json=data)
print(response.json()["choices"][0]["message"]["content"])