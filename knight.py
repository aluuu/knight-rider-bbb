import Adafruit_BBIO.GPIO as GPIO
import time

def setup(*pins):
    map(lambda pin: GPIO.setup("P9_%d" % pin, GPIO.OUT), pins)

def on(pin):
    GPIO.output("P9_%d" % pin, GPIO.HIGH)

def off(pin):
    GPIO.output("P9_%d" % pin, GPIO.LOW)

def timeout(sec):
    time.sleep(sec)

def reset(*pins):
    map(off, pins)

def knight_rider(pins, sec):

    for p in pins:
        on(p)
	timeout(sec)

    for p in pins:
        off(p)
	timeout(sec)

def start(*on_pins):
    '''
    start(12,14,16,22,24,26) - blink on 12,14,16... pins LEDs
    '''
    setup(on_pins)
    while True:
        knight_rider(on_pins, 0.03)
        knight_rider(list(reversed(on_pins)), 0.03)
