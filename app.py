from flask import Flask, render_template, request
import requests
import os
app = Flask(__name__)

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
	# Query
	q = request.form['q']
	# Add HTML formatting
	html = "\n Answer the question and format your answers nicely using HTML and not Markdown. Don't mention HTML."
	# Prepare the data to be sent (can be JSON, string, etc.)
	messages = [{"role": "user", "content": q + html}]
	data = {"messages": messages, "model": "llama3-70b-8192"}

	# Send the POST request with headers and data
	response = requests.post(url, headers=headers, json=data)

	# Check the response status code
	if response.status_code == 200:
		# Add CSS
		css = '<link href="/static/styles.css" rel="stylesheet">'
		# Access the response data (if any)
		response_data = response.json()
		# Access the message content from the response
		body = response_data["choices"][0]["message"]["content"]
		return css + body 
	else:
		return response.json()