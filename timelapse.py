import RPi.GPIO as GPIO
import time


PUL = 18
ENA = 23
DIR = 15


GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

GPIO.setup(PUL, GPIO.OUT)
#GPIO.setup(ENA, GPIO.OUT)
GPIO.setup(DIR, GPIO.OUT)
count = 0

while True:
	try:
		GPIO.setup(PUL, GPIO.IN)
		time.sleep(0.00005)
		GPIO.setup(PUL, GPIO.OUT)
		time.sleep(0.00005)
		count += 1
	except KeyboardInterrupt:
		break

print(count)
GPIO.cleanup()

