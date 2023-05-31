import threading
import subprocess
import RPi.GPIO as GPIO
import time

GPIO_TRIGGER = 18
GPIO_ECHO = 20
#GPIO_VIBRATION = 21

GPIO.setup(GPIO_TRIGGER, GPIO.OUT)
GPIO.setup(GPIO_ECHO, GPIO.IN)
#GPIO.setup(GPIO_VIBRATION, GPIO.OUT)

GPIO.setmode(GPIO.BCM)
GPIO.setup(22, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(23, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(24, GPIO.IN, pull_up_down=GPIO.PUD_UP)

def button_pressed(channel):
    if channel == 22:
        print("Button 1 pressed")
        subprocess.call("python Image_Captioning.py", shell=True)
    elif channel == 23:
        print("Button 2 pressed")
        subprocess.call("python Text_Extraction.py", shell=True)
    elif channel == 24:
        print("Button 3 pressed")
        subprocess.call("python file_no_3.py", shell=True)


def ultrasonic():


    while True:
        # set Trigger to HIGH
        GPIO.output(GPIO_TRIGGER, True)

        # set Trigger after 0.01ms to LOW
        time.sleep(0.00001)
        GPIO.output(GPIO_TRIGGER, False)

        StartTime = time.time()
        StopTime = time.time()

        # save StartTime
        while GPIO.input(GPIO_ECHO) == 0:
            StartTime = time.time()

        # save time of arrival
        while GPIO.input(GPIO_ECHO) == 1:
            StopTime = time.time()

        # time difference between start and arrival
        TimeElapsed = StopTime - StartTime
        # multiply with the sonic speed (34300 cm/s)
        # and divide by 2, because there and back
        distance = (TimeElapsed * 34300) / 2

        print("Distance: %.1f cm" % distance)

        if distance < 20:
            #GPIO.output(GPIO_VIBRATION, True)
            print("hii")
        else:
            #GPIO.output(GPIO_VIBRATION, False)
            print("nothing...")

        time.sleep(0.1)


if __name__ == '__main__':
    t1 = threading.Thread(target=button_pressed, args=(22,))
    t2 = threading.Thread(target=button_pressed, args=(23,))
    t3 = threading.Thread(target=button_pressed, args=(24,))
    t4 = threading.Thread(target=ultrasonic)

    t1.start()
    t2.start()
    t3.start()
    t4.start()

    t1.join()
    t2.join()
    t3.join()
    t4.join()
