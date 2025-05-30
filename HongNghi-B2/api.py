from flask import Flask, request, jsonify
from cipher.caesar import CaesarCipher 
from cipher.vigenere import VigenereCipher 
# from cipher.railfence import RailFenceCipher 
# from cipher.playfair import PlayFairCipher 
# from cipher.transposition import TranspositionCipher 

app = Flask(__name__) 

#CAESAR CIPHER ALGORITHM 
caesar_cipher = CaesarCipher() 

@app.route("/api/caesar/encrypt", methods=["POST"]) 
def caesar_encrypt(): 
    data = request.json 
    plain_text = data['plain_text'] 
    key = int(data['key']) 
    encrypted_text = caesar_cipher.encrypt_text(plain_text, key) 
    return jsonify({'encrypted_message': encrypted_text}) 

@app.route("/api/caesar/decrypt", methods=["POST"]) 
def caesar_decrypt(): 
    data = request.json 
    cipher_text = data['cipher_text'] 
    key = int(data['key']) 
    decrypted_text = caesar_cipher.decrypt_text(cipher_text, key) 
    return jsonify({'decrypted_message': decrypted_text})

#VIGENERE CIPHER ALGORITHM 
vigenere_cipher = VigenereCipher()

# API mã hóa Vigenère
@app.route('/api/vigenere/encrypt', methods=['POST'])
def vigenere_encrypt():
    data = request.json
    plain_text = data['plain_text']
    key = data['key']
    encrypted_text = vigenere_cipher.vigenere_encrypt(plain_text, key)
    return jsonify({'encrypted_text': encrypted_text})

# API giải mã Vigenère
@app.route('/api/vigenere/decrypt', methods=['POST'])
def vigenere_decrypt():
    data = request.json
    cipher_text = data['cipher_text']
    key = data['key']
    decrypted_text = vigenere_cipher.vigenere_decrypt(cipher_text, key)
    return jsonify({'decrypted_text': decrypted_text})
