import os
import easyocr
import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt
from gtts import gTTS

IMAGE_PATH = "Resources/good.jpeg"
language = 'en'
sentence = ""
font = cv.FONT_HERSHEY_SIMPLEX

reader = easyocr.Reader([language], gpu=False)
result = reader.readtext(IMAGE_PATH)

img = cv.imread(IMAGE_PATH)
spacer = 100
for detection in result:
    top_left = tuple(detection[0][0])
    bottom_right = tuple(detection[0][2])
    text = detection[1]
    sentence = sentence + " " + text
    img = cv.rectangle(img, top_left, bottom_right, (0, 255, 0), 3)
    img = cv.putText(img, text, (20, spacer), font, 0.5, (0, 255, 0), 2, cv.LINE_AA)
    spacer += 15

with open("output.txt", "w") as f:
    print(sentence, file=f)
sentence = ""

plt.imshow(img)
plt.show()

file = open('output.txt', 'r')
myText = file.read().replace("\n", " ")
output = gTTS(text=myText, lang=language, slow=False)
output.save("output.mp3")
os.system("start output.mp3")
