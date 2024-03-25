from flask import Flask, request, render_template_string
import openai
from llamaindex import LlamaIndex
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

app = Flask(__name__)

# Load the indexed PDF content
index = LlamaIndex()
index.load("pdf_index")

# Retrieve the OpenAI API key from environment variable
openai.api_key = os.getenv("OPENAI_API_KEY")

@app.route("/", methods=["GET"])
def home():
    return render_template_string("""
    <!DOCTYPE html>
    <html>
    <head>
        <title>PDF Query Interface</title>
    </head>
    <body>
        <h2>Ask a Question</h2>
        <form action="/ask" method="post">
            <input type="text" name="question" placeholder="Enter your question here" required>
            <input type="submit" value="Ask">
        </form>
    </body>
    </html>
    """)

@app.route("/ask", methods=["POST"])
def ask():
    question = request.form.get("question")
    
    # Retrieve relevant context from indexed PDFs
    context = index.search(question, top_k=3)  # Adjust top_k as needed
    
    # Use OpenAI's ChatGPT with the context to generate an answer
    response = openai.Completion.create(
        model="gpt-4",
        prompt=f"{question}\n\n###\n\n{context}",
        max_tokens=150,
        temperature=0.7
    )
    
    return f"Question: {question}<br>Answer: {response.choices[0].text.strip()}"

if __name__ == "__main__":
    app.run(debug=True)
