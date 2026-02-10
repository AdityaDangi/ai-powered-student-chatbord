from flask import Flask, request, render_template
from student_support_bot import student_support_bot

app = Flask(__name__)

# Stores conversation history per session
session_context = {}

@app.route("/", methods=["GET", "POST"])
def index():
    response = ""

    if request.method == "POST":
        user_input = request.form.get("message")
        response = student_support_bot(user_input, session_context)

    return render_template("index.html", response=response)

if __name__ == "__main__":
    app.run(debug=True)
