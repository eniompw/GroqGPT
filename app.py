from flask import Flask, render_template, request
import requests
import os
app = Flask(__name__)

@app.route('/debug')
def debug():
	return str(os.environ.get("GROQ_API_KEY"))[50:]

@app.route('/')
def home():
	return render_template('index.html')

@app.route('/query', methods=['POST'])
def query():
	
	# Define the URL for the POST request
	url = "https://api.groq.com/openai/v1/chat/completions"

	# Create a dictionary for headers
	headers = {
		"Content-Type": "application/json",  # Adjust content type as needed (e.g., application/xml)
		"Authorization": "Bearer " + str(os.environ.get("GROQ_API_KEY")),  # Your authorization token
	}

	q = request.form['q']
	# Prepare the data to be sent (can be JSON, string, etc.)
	messages = [{"role": "user", "content": q}]
	data = {"messages": messages, "model": "llama3-70b-8192"}

	# Send the POST request with headers and data
	response = requests.post(url, headers=headers, json=data)

	# Check the response status code
	if response.status_code == 200:
		# Access the response data (if any)
		response_data = response.json()
		return response_data["choices"][0]["message"]["content"]
	else:
		return response.json()