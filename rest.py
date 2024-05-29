import requests
import os

# Define the URL for the POST request
url = "https://api.groq.com/openai/v1/chat/completions"

# Create a dictionary for headers
headers = {
    "Content-Type": "application/json",  # Adjust content type as needed (e.g., application/xml)
    "Authorization": "Bearer " + str(os.environ.get("GROQ_API_KEY")),  # Your authorization token
}

q = input("Enter your question here: ")
# Prepare the data to be sent (can be JSON, string, etc.)
messages = [{"role": "user", "content": q}]
data = {"messages": messages, "model": "llama3-70b-8192"}

# Send the POST request with headers and data
response = requests.post(url, headers=headers, json=data)

# Check the response status code
if response.status_code == 200:
  # print("Success! Data posted.")
  # Access the response data (if any)
  response_data = response.json()
  print(response_data["choices"][0]["message"]["content"])
else:
  print("Error! Response code:", response.status_code)
  print(response.json())
