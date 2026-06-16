from flask import Flask, render_template, request

app = Flask(__name__)

def chatbot_response(user):
    user = user.lower()

    if "hi" in user or "hello" in user:
        return "Hello! How can I help you?"

    elif "your name" in user:
        return "My name is RuleBot."

    elif "how are you" in user:
        return "I am doing great!"

    elif "python" in user:
        return "Python is a popular programming language."

    elif "bye" in user:
        return "Goodbye!"

    else:
        return "Sorry, I don't understand."

@app.route("/", methods=["GET", "POST"])
def home():
    response = ""

    if request.method == "POST":
        user_message = request.form["message"]
        response = chatbot_response(user_message)

    return render_template("index.html", response=response)

if __name__ == "__main__":
    app.run(debug=True)