from flask import Flask, render_template, request, redirect, send_file, url_for
import base64
import os
from werkzeug.utils import secure_filename
from img_hidden import encrypt as steg_encrypt
from img_hidden import decrypt as steg_decrypt
from video_stego.encode_video import encode_video as video_encoder
from video_stego.decode_video import decode_video as video_decoder
from blockchain.blockchain import Blockchain

app = Flask(__name__)
UPLOAD_FOLDER = 'uploads'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/base64', methods=['GET', 'POST'])
def base64_tool():
    result = ''
    if request.method == 'POST':
        data = request.form['input_data']
        if 'encode' in request.form:
            result = base64.b64encode(data.encode()).decode()
        elif 'decode' in request.form:
            try:
                result = base64.b64decode(data.encode()).decode()
            except:
                result = 'Lỗi giải mã!'
    return render_template('base64.html', result=result)

@app.route('/img-hidden', methods=['GET', 'POST'])
def image_hidden():
    result = ''
    if request.method == 'POST':
        if 'hide' in request.form:
            file = request.files['image']
            message = request.form['message']
            if file:
                path = os.path.join(app.config['UPLOAD_FOLDER'], secure_filename(file.filename))
                file.save(path)
                original_name = os.path.basename(path)
                encoded_image_path = os.path.join(app.config['UPLOAD_FOLDER'], f"encoded_{original_name}")
                steg_encrypt.encode_image(path, message, output_path=encoded_image_path)

                return send_file(encoded_image_path, as_attachment=True)
        elif 'reveal' in request.form:
            try:
                encoded_image_path = os.path.join(os.getcwd(), 'encoded_image.png')
                msg = steg_decrypt.decode_image(encoded_image_path)
                result = msg
            except:
                result = 'Lỗi giải mã ảnh!'
    return render_template('img_hidden.html', result=result)

@app.route('/video-stego', methods=['GET', 'POST'])
def video_stego():
    result = ''
    if request.method == 'POST':
        if 'hide' in request.form:
            file = request.files['video']
            message = request.form['message']
            if file:
                path = os.path.join(app.config['UPLOAD_FOLDER'], secure_filename(file.filename))
                file.save(path)
                original_name = os.path.basename(path)
                name, ext = os.path.splitext(original_name)
                output = os.path.join(app.config['UPLOAD_FOLDER'], f"encoded_{name}.avi")
                video_encoder(path, output, message)
                return send_file(output, as_attachment=True)
        elif 'reveal' in request.form:
            file = request.files['video']
            if file:
                path = os.path.join(app.config['UPLOAD_FOLDER'], secure_filename(file.filename))
                file.save(path)
                msg = video_decoder(path)
                result = msg
    return render_template('video_stego.html', result=result)

@app.route('/blockchain')
def blockchain_demo():
    blockchain = Blockchain()
    blockchain.add_transaction("Alice", "Bob", 10)
    proof = blockchain.proof_of_work(blockchain.get_previous_block().proof)
    blockchain.create_block(proof, blockchain.get_previous_block().hash)
    return render_template('blockchain.html', chain=blockchain.chain)

if __name__ == '__main__':
    app.run(debug=True)
