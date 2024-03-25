from flask import Flask, request, render_template_string, session
from flask_session import Session  # You might need to install this with pip
import openai
from dotenv import load_dotenv
import os
from llama_index.core import (
    StorageContext,
    load_index_from_storage,
)

# Load environment variables from .env file
load_dotenv()

app = Flask(__name__)
# Secret key for sessions
app.config['SECRET_KEY'] = '38prgsrhgwh2v8tpwn8vtp843pv'  # Change this to a random secret key
# Session configuration (you can use the filesystem-based session for simplicity)
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

# Load the index
PERSIST_DIR = "./storage"
storage_context = StorageContext.from_defaults(persist_dir=PERSIST_DIR)
index = load_index_from_storage(storage_context)

@app.route("/", methods=["GET", "POST"])
def home():
    if 'history' not in session:
        session['history'] = []

    if request.method == "POST":
        question = request.form.get("question")
        print('question: ', question)

        # Example of querying the index; adapt this to your actual querying logic
        query_engine = index.as_query_engine()
        response = query_engine.query(question)
        print('Answer:' , response)

        # Insert at the beginning of the list to show on top
        session['history'].insert(0, (question, response))
        session.modified = True  # This is important to mark the session as modified

    return render_template_string("""
    <!DOCTYPE html>
    <html>
    <head>
        <title>PDF Query Interface</title>
        <style>
            body { font-family: Arial, sans-serif; margin: 0; padding: 0; background-color: #f9f9f9; }
            .container { max-width: 600px; margin: auto; padding: 20px; }
            h2 { color: #333; }
            form { margin-bottom: 20px; }
            input[type=text] { width: calc(100% - 122px); padding: 10px; margin-right: 10px; border: 1px solid #ddd; border-radius: 5px; }
            input[type=submit] { padding: 10px 20px; border: none; border-radius: 5px; background-color: #007BFF; color: white; cursor: pointer; }
            .history { margin-top: 20px; }
            .history div { background-color: white; padding: 10px; border-radius: 5px; margin-bottom: 10px; box-shadow: 0 2px 4px rgba(0,0,0,0.1); }
            .question { color: #007BFF; }
            .answer { color: #333; }
        </style>
    </head>
    <body>
        <div class="container">
            <h2>Ask a Question</h2>
            <form action="/" method="post">
                <input type="text" name="question" placeholder="Enter your question here" required>
                <input type="submit" value="Ask">
            </form>
            <div class="history">
                {% for q, a in session['history'] %}
                <div>
                    <div class="question">{{ q }}</div>
                    <div class="answer">{{ a }}</div>
                </div>
                {% endfor %}
            </div>
        </div>
    </body>
    </html>
    """, history=session['history'])

if __name__ == "__main__":
    app.run(debug=True)
