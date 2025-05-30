from flask import Flask, render_template, request
from cipher.caesar import CaesarCipher
from cipher.vigenere import VigenereCipher

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/caesar", methods=["POST"])
def caesar():
    caesar_result = ""
    caesar_action = request.form.get("action")
    caesar_text = request.form.get("text", "")
    caesar_key = int(request.form.get("key", 0))
    
    cipher = CaesarCipher()
    
    try:
        if caesar_action == "encrypt_caesar":
            caesar_result = cipher.encrypt_text(caesar_text, caesar_key)
        elif caesar_action == "decrypt_caesar":
            caesar_result = cipher.decrypt_text(caesar_text, caesar_key)
    except Exception as e:
        caesar_result = f"Lỗi: {str(e)}"
    
    return render_template("index.html", 
                         caesar_result=caesar_result,
                         caesar_text=caesar_text,
                         caesar_key=caesar_key,
                         caesar_action=caesar_action)

@app.route("/vigenere", methods=["POST"])
def vigenere():
    vigenere_result = ""
    vigenere_action = request.form.get("action")
    vigenere_text = request.form.get("text", "")
    key = request.form.get("key", "").strip()
    
    if not key:
        vigenere_result = "Lỗi: Vui lòng nhập khóa cho Vigenere cipher!"
    else:
        cipher = VigenereCipher()
        
        try:
            if vigenere_action == "encrypt_vigenere":
                vigenere_result = cipher.vigenere_encrypt(vigenere_text, key)
            elif vigenere_action == "decrypt_vigenere":
                vigenere_result = cipher.vigenere_decrypt(vigenere_text, key)
        except Exception as e:
            vigenere_result = f"Lỗi: {str(e)}"
    
    return render_template("index.html",
                         vigenere_result=vigenere_result,
                         vigenere_text=vigenere_text,
                         vigenere_action=vigenere_action,
                         key=key)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=2058, debug=True)