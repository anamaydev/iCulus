# USED TO TEST APIs on cloud

import requests


# resp = requests.post("http://172.20.10.3:8080/getres", files={'image': open(r'F:\codes\Projects\Captioning\Hackathon\test.png', 'rb')})

# resp = requests.post("https://kalesh1-de4l3khwaa-uc.a.run.app/getres", files={'image': open(r'C:\Users\lolling\Pictures\Screenshot.png', 'rb')})

# resp = requests.post("http://ec2-100-24-26-222.compute-1.amazonaws.com:8080/getres", files={'image': open(r'C:\Users\lolling\Downloads\hjfbd.jpeg', 'rb')})
resp = requests.post("https://kaleshocr-de4l3khwaa-el.a.run.app/getres", files={'image': open(r'C:\Users\lolling\Downloads\notice2.jpeg', 'rb')})

print(resp.text)

file = open("response.txt", "w")
a = file.write(resp.text)
file.close()
