from fileinput import filename
from flask import Flask, jsonify, request, send_file, redirect, send_from_directory
from dotenv import load_dotenv
import os
from werkzeug.utils import secure_filename

load_dotenv('../.env')

UPLOAD_FOLDER = 'static/uploads'
ACCESS_TOKEN = os.environ['ACCESS_TOKEN']

app = Flask(__name__)
app.secret_key = ACCESS_TOKEN
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@app.route('/upload', methods=['POST'])
def upload_file():
    model = {
        "type": "image",
        "key": "",
        "name": "image1"
    }
    res = []
    files = request.files

    if len(files) > 0:
        for (key, file) in files.items():
            filename = secure_filename(file.filename)

            # save the metadata
            model['type'] = file.content_type
            model['key'] = key
            model['name'] = filename
            res.append(model)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))

        return jsonify(res), 200

# @app.route('/upload/<file_name>', methods=["GET"])
# def display_file(file_name):
#     return send_from_directory('./static/uploads', file_name)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001, debug=True)