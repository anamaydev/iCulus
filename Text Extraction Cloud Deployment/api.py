from flask import Flask
import flask
import werkzeug
import easyocr
import cv2 as cv

img_path = './img/'
    

app = Flask(__name__)

@app.route('/')
def home():
    return 'hi'

def predict(filename):
    language = 'en'
    sentence = ""
    reader = easyocr.Reader([language], gpu=False)
    result = reader.readtext(filename)
    img = cv.imread(filename)

    for detection in result:
        text = detection[1]
        sentence = sentence + " " + text
    return sentence

   

@app.route('/getres', methods = ['POST'])
def handle_request():
    imagefile = flask.request.files['image']
    filename = werkzeug.utils.secure_filename(imagefile.filename)
    print("\nReceived image File name : " + imagefile.filename)
    print(img_path+filename)
    imagefile.save(img_path+filename)
    ans = predict(img_path+filename)
    return ans
    
if __name__ == '__main__':
    app.run(host="0.0.0.0", port=8080, debug=True)
