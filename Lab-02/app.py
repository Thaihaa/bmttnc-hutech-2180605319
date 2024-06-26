from flask import Flask, render_template, request
from cipher.caesar import CaesarCipher
from cipher.vigenere import VigenereCipher
from cipher.railfence import RailFenceCipher

app = Flask(__name__)

@app.route("/")
def home():
    return render_template('index.html')

#CAESAR
@app.route("/caesar")
def caesar():
    return render_template('caesar.html')

@app.route("/encrypt", methods=['POST'])
def caesar_encrypt():
    text = request.form['inputPlainText']
    key = int(request.form['inputKeyPlain'])  # Ensure key is an integer
    caesar_cipher = CaesarCipher()
    encrypted_text = caesar_cipher.encrypt_text(text, key)
    return f"text: {text}<br/>key: {key}<br/>encrypted text: {encrypted_text}"

@app.route("/decrypt", methods=['POST'])
def caesar_decrypt():
    text = request.form['inputCipherText']
    key = int(request.form['inputKeyCipher'])  # Ensure key is an integer
    caesar_cipher = CaesarCipher()
    decrypted_text = caesar_cipher.decrypt_text(text, key)
    return f"text: {text}<br/>key: {key}<br/>decrypted text: {decrypted_text}"

#VIGENERE
@app.route("/vigenere")
def vigenere():
    return render_template('vigenere.html')

@app.route("/vigenere/encrypt", methods=['POST'])
def vigenere_encrypt():
    text = request.form['inputPlainText']
    key = request.form['inputKeyEncrypt']
    vigenere_cipher = VigenereCipher()
    encrypted_text = vigenere_cipher.encrypt_text(text, key)
    return f"text: {text}<br/>key: {key}<br/>encrypted text: {encrypted_text}"

@app.route("/vigenere/decrypt", methods=['POST'])
def vigenere_decrypt():
    text = request.form['inputCipherText']
    key = request.form['inputKeyDecrypt']
    vigenere_cipher = VigenereCipher()
    decrypted_text = vigenere_cipher.decrypt_text(text, key)
    return f"text: {text}<br/>key: {key}<br/>decrypted text: {decrypted_text}"

#RAIL FENCE
@app.route("/railfence")
def railfence():
    return render_template('railfence.html')

@app.route("/encrypt_railfence", methods=['POST'])
def encrypt_railfence():
    text = request.form['inputPlainText']
    rails = int(request.form['numRails']) 
    railfence_cipher = RailFenceCipher()
    encrypted_text = railfence_cipher.encrypt(text, rails)
    return f"text: {text}<br/>rails: {rails}<br/>encrypted text: {encrypted_text}"

@app.route("/decrypt_railfence", methods=['POST'])
def decrypt_railfence():
    text = request.form['inputCipherText']
    rails = int(request.form['numRails'])  
    railfence_cipher = RailFenceCipher()
    decrypted_text = railfence_cipher.decrypt(text, rails)
    return f"text: {text}<br/>rails: {rails}<br/>decrypted text: {decrypted_text}"

# Main function
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5050, debug=True)
