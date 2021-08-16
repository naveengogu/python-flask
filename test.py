
from flask import Flask, render_template, request, send_file, send_from_directory
import boto3
app = Flask(__name__)
from werkzeug.utils import secure_filename
# import key_config as keys

UPLOAD_FOLDER = "/Users/naveengogu/Documents/python_POC/rnd/AWS-Flask2"

s3 = boto3.client('s3',
                    aws_access_key_id='####',
                    aws_secret_access_key='####'
                    # aws_session_token=keys.AWS_SESSION_TOKEN
                     )

BUCKET_NAME='source-bucket-python-images-naveengogu'

@app.route('/')  
def home():
    return render_template("file_upload_to_s3.html")

@app.route('/upload',methods=['post'])
def upload():
    if request.method == 'POST':
        img = request.files['file']
        if img:
                filename = secure_filename(img.filename)
                img.save(filename)
                s3.upload_file(
                    Bucket = BUCKET_NAME,
                    Filename=filename,
                    Key = filename
                )
                msg = "Upload Done ! "
                # msg = filename

    return render_template("file_upload_to_s3.html",filename =filename)

# app.route('/uploads/<filename>')
# def uploaded_file(filename):
#     filename = 'http://127.0.0.1:5000/uploads/' + filename
#     return render_template('file_upload_to_s3.html', filename = filename)

# @app.route('/uploads/<filename>')
# def send_file(filename):
#     return send_from_directory(UPLOAD_FOLDER, filename)


if __name__ == "__main__":
    
    app.run(debug=True)


