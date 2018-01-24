import os

from flask import Flask, request, redirect, url_for
from werkzeug.utils import secure_filename

app = Flask(__name__)

app.secret_key = 'h9183rb02087B*^T&^!&Y@*&#GRD'

app.config['UPLOAD_FOLDER'] = os.path.join(
    os.path.dirname(os.path.abspath(__name__)),
    'uploaded'
)

ALLOWED_EXTENSIONS = ['csv']


def allowed_file(f):
    return f.rsplit('.')[-1] in ALLOWED_EXTENSIONS


@app.route('/', methods=['GET', 'POST'])
def upload_file(filename=None):
    if request.method == 'POST':
        if 'file' not in request.files:
            print('No file part')
            return redirect(request.url)
        f = request.files['file']
        if f.filename == '':
            print('No selected file')
            return redirect(request.url)
        if f and allowed_file(f.filename):
            filename = secure_filename(f.filename)
            f.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            print('upload successfull')
            return redirect(url_for('upload_file', filename=filename))

    return '''
    <!DOCTYPE html>
    <title>Upload new file</title>
    <h1>Upload new file</h1>
    <form method=post enctype=multipart/form-data>
        <p><input type=file name=file>
        <input type=submit value=Upload>
    </form>
    '''


if __name__ == '__main__':
    app.run(debug=True)
