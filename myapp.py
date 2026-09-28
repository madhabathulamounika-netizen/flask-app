from flask import Flask, request, session
from datetime import timedelta

app = Flask(__name__)

app.secret_key = "mounika-secret-key"

app.config["PERMANENT_SESSION_LIFETIME"] = timedelta(days=3650)


@app.route("/", methods=["GET", "POST"])
def home():

    if request.method == "POST":
        name = request.form["name"]

        session.permanent = True
        session["name"] = name

        return f"Hello {name}! 👋 Nice to meet you!"

    return """
    <h1>✨ My Flask App ✨</h1>

    <form method="POST">
        <label>Enter your name:</label>
        <input type="text" name="name" required>
        <button type="submit">Greet Me</button>
    </form>
    """


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
