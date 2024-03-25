from flask import Flask, request, render_template_string
import openai
from dotenv import load_dotenv
import os
from llama_index.core import (
    VectorStoreIndex,
    SimpleDirectoryReader,
    StorageContext,
    load_index_from_storage,
)

# Load environment variables from .env file
load_dotenv()

app = Flask(__name__)

# load the the index
PERSIST_DIR = "./storage"
storage_context = StorageContext.from_defaults(persist_dir=PERSIST_DIR)
index = load_index_from_storage(storage_context)


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
    
    # # Retrieve relevant context from indexed PDFs
    # context = index.search(question, top_k=3)  # Adjust top_k as needed
    
    # # Use OpenAI's ChatGPT with the context to generate an answer
    # response = openai.Completion.create(
    #     model="gpt-4",
    #     prompt=f"{question}\n\n###\n\n{context}",
    #     max_tokens=150,
    #     temperature=0.7
    # )

    # Either way we can now query the index
    query_engine = index.as_query_engine()
    response = query_engine.query(question)
    print(response)
    
    return f"Question: {question}<br>Answer: {response}"

if __name__ == "__main__":
    app.run(debug=True)
