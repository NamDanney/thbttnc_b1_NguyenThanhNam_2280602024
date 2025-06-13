from flask import Flask, render_template, request, json
from ex01.cipher.caesar import CaesarCipher
from ex01.cipher.vigenere import VigenereCipher
from ex01.cipher.railfence import RailFenceCipher
from ex01.cipher.playfair import PlayfairCipher
from ex01.cipher.transposition import TranspositionCipher 

app = Flask(__name__)

#router routes for home page
@app.route("/")
def home():
    return render_template("index.html")

#router routes for caesar cypher
@app.route("/caesar")
def caesar():
    return render_template("caesar.html")

@app.route("/encrypt", methods=["POST"])
def caesar_encrypt():
    text = request.form["inputPlainText"]
    key = int(request.form["inputKeyPlain"])
    Caesar = CaesarCipher()
    encrypted_text = Caesar.encrypt_text(text, key)
    return f"text: {text}<br/>key: {key}<br/>encrypted text: {encrypted_text}"

@app.route("/decrypt", methods=["POST"])
def caesar_decrypt():
    text = request.form["inputCipherText"]
    key = int(request.form["inputKeyCipher"])
    Caesar = CaesarCipher()
    decrypted_text = Caesar.decrypt_text(text, key)
    return f"text: {text}<br/>key: {key}<br/>decrypted text: {decrypted_text}"

# Thêm các router routes for vigenere cipher
@app.route("/vigenere")
def vigenere():
    return render_template("vigenere.html")

@app.route("/vigenere/encrypt", methods=["POST"])
def vigenere_encrypt():
    text = request.form["inputPlainTextVigenere"]
    key = request.form["inputKeyVigenerePlain"] # Key của Vigenere là chuỗi
    v_cipher = VigenereCipher()
    encrypted_text = v_cipher.vigenere_encrypt(text, key)
    return f"text: {text}<br/>key: {key}<br/>encrypted text: {encrypted_text}"

@app.route("/vigenere/decrypt", methods=["POST"])
def vigenere_decrypt():
    text = request.form["inputCipherTextVigenere"]
    key = request.form["inputKeyVigenereCipher"] # Key của Vigenere là chuỗi
    v_cipher = VigenereCipher()
    decrypted_text = v_cipher.vigenere_decrypt(text, key)
    return f"text: {text}<br/>key: {key}<br/>decrypted text: {decrypted_text}"

# Thêm các router routes for railfence cipher
@app.route("/railfence")
def railfence():
    return render_template("railfence.html")

@app.route("/railfence/encrypt", methods=["POST"])
def railfence_encrypt():
    text = request.form["inputPlainTextRailFence"]
    key = int(request.form["inputKeyRailFence"]) # Key là số lượng rails
    rf_cipher = RailFenceCipher()
    encrypted_text = rf_cipher.rail_fence_encrypt(text, key)
    return f"text: {text}<br/>key: {key}<br/>encrypted text: {encrypted_text}"

@app.route("/railfence/decrypt", methods=["POST"])
def railfence_decrypt():
    text = request.form["inputCipherTextRailFence"]
    key = int(request.form["inputKeyRailFenceDecrypt"]) # Key là số lượng rails
    rf_cipher = RailFenceCipher()
    decrypted_text = rf_cipher.rail_fence_decrypt(text, key)
    return f"text: {text}<br/>key: {key}<br/>decrypted text: {decrypted_text}"

# Thêm các router routes for playfair cipher
@app.route("/playfair")
def playfair():
    return render_template("playfair.html")

@app.route("/playfair/encrypt", methods=["POST"])
def playfair_encrypt_app():
    text = request.form["inputPlainTextPlayfair"]
    key = request.form["inputKeyPlayfair"]
    
    pf_cipher = PlayfairCipher() # Sửa ở đây
    playfair_matrix = pf_cipher.create_playfair_matrix(key)
    encrypted_text = pf_cipher.playfair_encrypt(text, playfair_matrix)
    
    return f"Plain Text: {text}<br/>Key: {key}<br/>Encrypted Text: {encrypted_text}<br/><br/>Playfair Matrix:<br/>" + "<br/>".join([" ".join(row) for row in playfair_matrix])

@app.route("/playfair/decrypt", methods=["POST"])
def playfair_decrypt_app():
    text = request.form["inputCipherTextPlayfair"]
    key = request.form["inputKeyPlayfairDecrypt"]
    
    pf_cipher = PlayfairCipher() 
    playfair_matrix = pf_cipher.create_playfair_matrix(key)
    decrypted_text = pf_cipher.playfair_decrypt(text, playfair_matrix)
    
    return f"Cipher Text: {text}<br/>Key: {key}<br/>Decrypted Text: {decrypted_text}<br/><br/>Playfair Matrix:<br/>" + "<br/>".join([" ".join(row) for row in playfair_matrix])

# Thêm các router routes for transposition cipher
@app.route("/transposition")
def transposition():
    return render_template("transposition.html")

@app.route("/transposition/encrypt", methods=["POST"])
def transposition_encrypt_app():
    text = request.form["inputPlainTextTransposition"]
    key = int(request.form["inputKeyTransposition"])
    
    t_cipher = TranspositionCipher()
    encrypted_text = t_cipher.encrypt(text, key)
    
    return f"Plain Text: {text}<br/>Key: {key}<br/>Encrypted Text: {encrypted_text}"

@app.route("/transposition/decrypt", methods=["POST"])
def transposition_decrypt_app():
    text = request.form["inputCipherTextTransposition"]
    key = int(request.form["inputKeyTranspositionDecrypt"])
    
    t_cipher = TranspositionCipher()
    decrypted_text = t_cipher.decrypt(text, key)
    
    return f"Cipher Text: {text}<br/>Key: {key}<br/>Decrypted Text: {decrypted_text}"

#main function
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=2024, debug=True)