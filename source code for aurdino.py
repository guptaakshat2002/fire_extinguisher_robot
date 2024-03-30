/*------ Arduino for automatic fire extinguisher Robot Code ---- */
 
import serial
import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)
GPIO.setup(7, GPIO.IN)  # GAS_SENSOR
GPIO.setup(11, GPIO.OUT)  # LM1
GPIO.setup(12, GPIO.OUT)  # LM2
GPIO.setup(13, GPIO.OUT)  # RM1
GPIO.setup(15, GPIO.OUT)  # RM2
GPIO.setup(16, GPIO.OUT)  # pump

ser = serial.Serial('/dev/ttyS0', 9600, timeout=1)

def put_off_fire():
    GPIO.output(11, GPIO.HIGH)
    GPIO.output(12, GPIO.HIGH)
    GPIO.output(13, GPIO.HIGH)
    GPIO.output(15, GPIO.HIGH)
    GPIO.output(16, GPIO.HIGH)
    time.sleep(0.5)
    for pos in range(50, 111):
        GPIO.output(13, GPIO.HIGH)
        time.sleep(0.01)
    for pos in range(110, 49, -1):
        GPIO.output(13, GPIO.HIGH)
        time.sleep(0.01)
    GPIO.output(16, GPIO.LOW)
    GPIO.output(13, GPIO.HIGH)

def make_call():
    print("calling....")
    ser.write(b'ATD' + PHONE.encode() + b';')
    time.sleep(20)
    ser.write(b'ATH')
    time.sleep(1)

def send_sms():
    print("sending sms....")
    time.sleep(0.05)
    ser.write(b'AT+CMGF=1\r')
    time.sleep(1)
    ser.write(b'AT+CMGS="' + PHONE.encode() + b'"\r')
    time.sleep(1)
    ser.write(b'Gas Detected')
    time.sleep(0.1)
    ser.write(b'\x1A')
    time.sleep(5)

try:
    while True:
        if GPIO.input(7) == 0:
            print("Gas is Detected.")
            send_sms()
        time.sleep(0.4)
except KeyboardInterrupt:
    GPIO.cleanup()

