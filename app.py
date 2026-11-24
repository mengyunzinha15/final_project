
from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")


@app.route("/learn", methods=["POST"])
def learn():
    language = request.form.get("language")

    language_names = {
        "english": "English",
        "portuguese": "Portuguese",
        "french": "French",
        "spanish": "Spanish",
        "mandarin": "Mandarin Chinese",
        "japanese": "Japanese",
        "german": "German"
    }

    selected_language = language_names.get(language, "Language")

    return render_template(
        "learn.html",
        language=selected_language
    )


if __name__ == "__main__":
    app.run(debug=True)
