import time
import telebot
from luma.core.interface.serial import spi
from tempo import read_temp
from luma.oled.device import ssd1306
from luma.core.render import canvas
from PIL import ImageFont
import RPi.GPIO as GPIO
import sys
from tempo import read_temp
from bot import bot
from bot import alert_message
from datetime import datetime
from distance import measure_distance
import threading
import os

#SPI options
RST_PIN = 26 
DC_PIN = 21 
SPI_PORT = 0
SPI_DEVICE = 0
SPEAKER = 27

#gpio setup
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
OFF = 20
SHOW_TEMP = 16
GPIO.setup(OFF, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(SPEAKER, GPIO.OUT)
GPIO.setup(SHOW_TEMP, GPIO.IN, pull_up_down=GPIO.PUD_UP)
running = True

#SPI interface
serial = spi(device=SPI_DEVICE, port=SPI_PORT, gpio_DC=DC_PIN, gpio_RST=RST_PIN)
fpath = "/usr/share/fonts/truetype/roboto/unhinted/RobotoTTF/Roboto-Regular.ttf"
fsize = 45
font = ImageFont.truetype(fpath, fsize)
device = ssd1306(serial)


def addText(text):
    with canvas(device) as draw:
        draw.text((0, 7), text, font=font, fill=255)


#bot setup
        
def start_bot():
    bot.polling()

bot_t = threading.Thread(target=start_bot)
bot_t.start()

# distance setup

def find_distance():
    timer_d = 0
    global running
    while running:
        timer_d+=1
        
        if(timer_d > 1000):
            timer_d = 0
        
        dist = measure_distance()
        if(dist > 10):
            GPIO.output(SPEAKER, 1)
        else:
            GPIO.output(SPEAKER, 0)
        if(dist > 10 and timer_d > 10):
            alert_message()
            timer_d = 0
        time.sleep(1)

distance_t = threading.Thread(target=find_distance)
distance_t.start()
    
prev_state_tempo = GPIO.input(SHOW_TEMP)
cleat_time = 0

# welcome
addText("Start...")
time.sleep(2)
addText("")

#main loop
while running:
    cleat_time+=0.1
    if(cleat_time > 5):
        with canvas(device) as draw:
            pass
    
    if(GPIO.input(OFF) == 0):
        running = False
        addText("Bye !")
        time.sleep(2)
        with canvas(device) as draw:
            pass
        os.system("sudo shutdown -h now")
        
   
    if(prev_state_tempo == 1 and GPIO.input(SHOW_TEMP) == 0):
        cleat_time = 0
        addText(f"{read_temp()} C")
        
    prev_state_tempo = GPIO.input(SHOW_TEMP)
    time.sleep(0.1)