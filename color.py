import requests
from bs4 import BeautifulSoup
import RPi.GPIO as GPIO
import time

def set_led_color(hex_color):
    if len(hex_color) == 7 and hex_color[0] == "#":
        try:
            red_value = int(hex_color[1:3], 16) * 100 / 255
            green_value = int(hex_color[3:5], 16) * 100 / 255
            blue_value = int(hex_color[5:7], 16) * 100 / 255

            red.ChangeDutyCycle(red_value)
            green.ChangeDutyCycle(green_value)
            blue.ChangeDutyCycle(blue_value)
        except ValueError:
            print("")
    else:
        print("Enter data like #ff34b1")
 
def reset_return():
    url_path = 'https://www.steamclown.org/projects/QInlIj_vIHev/Huch_QIn/' 
    url_file = 'all_robots_command_requests.txt'
    url = url_path + url_file
    r = requests.get(url)

    whole_file = r.text
    lines = whole_file.split("\n")
    for line in lines:
        print('hi')
        line_list = line.split(',')
        if line_list[0] == "Luis-Mechatronics":
            hex_color = line_list[2].strip()
            set_led_color(hex_color)
            time.sleep(.2)
            
           

GPIO.setmode(GPIO.BOARD)

RED = 33
GREEN = 29
BLUE = 31

GPIO.setup(RED, GPIO.OUT)
GPIO.setup(GREEN, GPIO.OUT)
GPIO.setup(BLUE, GPIO.OUT)

red = GPIO.PWM(RED, 100)
green = GPIO.PWM(GREEN, 100)
blue = GPIO.PWM(BLUE, 100)

red.start(0)
green.start(0)
blue.start(0)

reset_return()

def #:
code = "61 69 63 72 61 47 20 6f 64 6e 61 6d 72 41 20 73 69 75 4c"

N = ""
codes = code.split()

for value in codes:
    values = int(value, 16) 
    c = chr(values)     
    N = c + N           




         



