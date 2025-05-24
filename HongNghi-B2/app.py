from flask import Flask, render_template, request
from cipher.caesar import CaesarCipher

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def home():
    result = ""
    action = ""
    text = ""
    key = 0

    if request.method == "POST":
        action = request.form.get("action")
        key = int(request.form.get("key"))
        text = request.form.get("text")
        cipher = CaesarCipher()

        if action == "encrypt":
            result = cipher.encrypt_text(text, key)
        elif action == "decrypt":
            result = cipher.decrypt_text(text, key)

    return render_template("index.html", result=result, text=text, key=key, action=action)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=2058, debug=True)
