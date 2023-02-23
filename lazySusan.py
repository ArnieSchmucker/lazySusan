from machine import Pin, PWM
from utime import sleep

motorA = PWM(Pin(15))
dirA1=Pin(14, Pin.OUT)
dirA2=Pin(13, Pin.OUT)
motorA.freq(1000)
encoderA = Pin(16, Pin.IN);
encoderB = Pin(17, Pin.IN);
switchR = Pin(9, Pin.IN, Pin.PULL_UP)
switchL = Pin(5, Pin.IN, Pin.PULL_UP)
switchH = Pin(7, Pin.IN, Pin.PULL_UP)
switchSR = Pin(8, Pin.IN, Pin.PULL_UP)
switchSL = Pin(6, Pin.IN, Pin.PULL_UP)
counterA = 0
switchR.value(1)
switchL.value(1)
switchH.value(1)
switchSR.value(1)
dirIndicator = 0
maxCounter = 2700
pwmVal=(int)(65535)

def encoderAHandler(pin):
    global counterA
    if encoderB.value() == False:
        counterA += 1
    else:
        counterA -= 1
        
encoderA.irq(trigger=Pin.IRQ_RISING, handler=encoderAHandler)

while True:
    #Switch R
    if (switchR.value() == 0 and switchL.value() == 1 and switchH.value() == 1 and switchSR.value() == 1 and switchSL.value() == 1):
        print(counterA)
        dirA1.value(1)
        dirA2.value(0)
        motorA.duty_u16(pwmVal)
        sleep(.01)
    #Switch L
    elif (switchR.value() == 1 and switchL.value() == 0 and switchH.value() == 1 and switchSR.value() == 1 and switchSL.value() == 1):
        print(counterA)
        dirA1.value(0)
        dirA2.value(1)
        motorA.duty_u16(pwmVal)       
        sleep(.01)
    #Switch H
    elif (switchR.value() == 1 and switchL.value() == 1 and switchH.value() == 0 and switchSR.value() == 1 and switchSL.value() == 1):
        if (counterA <= 0):
            print(counterA)
            dirA1.value(0)
            dirA2.value(1)
        else:
            print(counterA)
            dirA1.value(1)
            dirA2.value(0)
        motorA.duty_u16(pwmVal)   
        sleep(.01)
    #Switch SR
    elif (switchR.value() == 1 and switchL.value() == 1 and switchH.value() == 1 and switchSR.value() == 0 and switchSL.value() == 1):
        print(counterA)
        dirA1.value(1)
        dirA2.value(0)
        motorA.duty_u16((int)(pwmVal/2))
        sleep(.01)
        motorA.duty_u16(0)
        sleep(.01)
        counterA = 0
    #Switch SL  
    elif (switchR.value() == 1 and switchL.value() == 1 and switchH.value() == 1 and switchSR.value() == 1 and switchSL.value() == 0):
        print(counterA)
        dirA1.value(0)
        dirA2.value(1)
        motorA.duty_u16((int)(pwmVal/2))
        sleep(.01)
        motorA.duty_u16(0)
        sleep(.01)
        counterA = 0        
    else:
        motorA.duty_u16(0)
        sleep(.01)

        