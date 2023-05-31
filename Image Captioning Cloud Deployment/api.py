from transformers import pipeline
from flask import Flask
import flask
import werkzeug

model_path = './model'
img_path = './img/'
    

app = Flask(__name__)

@app.route('/')
def home():
    return 'hi'

def predict(filename):
    path = img_path+filename   
    image_to_text = pipeline("image-to-text", model=model_path)
    print(path)
    return image_to_text(path)[0]['generated_text']

@app.route('/getres', methods = ['POST'])
def handle_request():
    imagefile = flask.request.files['image']
    filename = werkzeug.utils.secure_filename(imagefile.filename)
    print("\nReceived image File name : " + imagefile.filename)
    imagefile.save(img_path+filename)
    ans = predict(filename)
    return ans
    
if __name__ == '__main__':
    app.run(host="0.0.0.0", port=8080, debug=True)
