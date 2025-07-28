from flask import Flask, request, send_file, render_template
from werkzeug.utils import secure_filename
import os
from docx2pdf import convert

app = Flask(__name__)

UPLOAD_FOLDER = 'uploads/'
CONVERTED_FOLDER = 'converted/'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['CONVERTED_FOLDER'] = CONVERTED_FOLDER

if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)

if not os.path.exists(CONVERTED_FOLDER):
    os.makedirs(CONVERTED_FOLDER)

@app.route('/')
def upload_file():
    return render_template('index.html')

@app.route('/convert', methods=['POST'])
def convert_file():
    if 'file' not in request.files:
        return "No file part"

    file = request.files['file']
    if file.filename == '':
        return "No selected file"

    if file:
        filename = secure_filename(file.filename)
        word_file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        file.save(word_file_path)

        # Convert Word to PDF
        pdf_filename = filename.rsplit('.', 1)[0] + '.pdf'
        pdf_file_path = os.path.join(app.config['CONVERTED_FOLDER'], pdf_filename)
        convert(word_file_path, pdf_file_path)

        return send_file(pdf_file_path, as_attachment=True)

if __name__ == "__main__":
    app.run(debug=True)
