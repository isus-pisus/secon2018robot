from RPLCD import CharLCD
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)
GPIO.setup(24, GPIO.OUT)
GPIO.setup(26, GPIO.OUT)
GPIO.setup(23, GPIO.OUT)
GPIO.setup(17, GPIO.OUT)
GPIO.setup(27, GPIO.OUT)
GPIO.setup(22, GPIO.OUT)
GPIO.setwarnings(False)

lcd = CharLCD(cols=16, rows=2, pin_rs=26, pin_e=24, pins_data=[23, 17, 27, 22], numbering_mode=GPIO.BCM)
