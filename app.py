from flask import Flask, render_template, request
import os
from groq import Groq

app = Flask(__name__)
groq_client = Groq(api_key=os.environ.get("GROQ_API_KEY"))

@app.route('/')
def home():
	return render_template('index.html')

@app.route('/query')
def query():
	q = request.args.get('q') + " (use HTML to nicely format the response)"
	chat_completion = groq_client.chat.completions.create(
		messages=[{"role": "user", "content": q}],
		model="openai/gpt-oss-120b",
	)
	return chat_completion.choices[0].message.content

if __name__ == '__main__':
    app.run(debug=True)
