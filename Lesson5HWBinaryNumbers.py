import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)

GPIOPin0 = 11
GPIOPin2 = 13
GPIOPin4 = 15
GPIOPin8 = 29
GPIOPin16 = 31

Delay = 1.0
ON = 1
OFF = 0
COUNTER = 0
ADDER = 1
LOOPS = int(input("How many cycles do you wish: "))

GPIO.setup(GPIOPin0, GPIO.OUT)
GPIO.setup(GPIOPin2, GPIO.OUT)
GPIO.setup(GPIOPin4, GPIO.OUT)
GPIO.setup(GPIOPin8, GPIO.OUT)
GPIO.setup(GPIOPin16, GPIO.OUT)

while LOOPS:
    print("Counter: ", COUNTER)
    print("Loop: ", LOOPS)
    print("ADDER: ", ADDER)
    if COUNTER & 0b10000:
        GPIO.output(GPIOPin16, ON)
        print("1000")
    if COUNTER & 0b01000:
        GPIO.output(GPIOPin8, ON)
        print("1000")
    if COUNTER & 0b00100:
        GPIO.output(GPIOPin4, ON)
        print("100")
    if COUNTER & 0b00010:
        GPIO.output(GPIOPin2, ON)
        print("10")
    if COUNTER & 0b00001:
        GPIO.output(GPIOPin0, ON)
        print("1")
    time.sleep(Delay)
    GPIO.output(GPIOPin0, OFF)
    GPIO.output(GPIOPin2, OFF)
    GPIO.output(GPIOPin4, OFF)
    GPIO.output(GPIOPin8, OFF)
    GPIO.output(GPIOPin16, OFF)
    COUNTER = COUNTER + ADDER
    if COUNTER > 31 or COUNTER < 0:
        ADDER = ADDER * (-1)
        LOOPS = LOOPS - 1
        if ADDER > 0:
            COUNTER = 0

GPIO.cleanup()
