# Main program for preamp
import board
from time import sleep
import rotaryio
import pulseio
import digitalio

VOLUME = -1
SOURCE = 1
DOWN = -1
UP = 1

mode = VOLUME

def volume(increment):
    # Increment or decrement volume
    pass

def source(increment):
    # Increment or decrement source
    pass

# Main loop
while True:
    r = r.getvalue()
    if mode == VOLUME:
        volume(r)
    elif mode == SOURCE:
        source(r)
    if r.pressed():
        mode = -mode
    sleep(0.1)