
from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/learn", methods=["POST"])
def learn():
    language = request.form.get("language")

    return f"You selected: {language.title()}"

if __name__ == "__main__":
    app.run(debug=True)
