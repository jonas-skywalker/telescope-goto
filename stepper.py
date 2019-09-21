import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

PUL = 18
ENA = 23
DIR = 15


GPIO.setup(PUL, GPIO.OUT)
#GPIO.setup(ENA, GPIO.OUT)
GPIO.setup(DIR, GPIO.OUT)


print("STARTING...")


for i in range(6400):
	GPIO.setup(PUL, GPIO.OUT)
	# GPIO.output(ENA, GPIO.HIGH)
	# GPIO.output(PUL, GPIO.HIGH)
	time.sleep(0.00005)
	GPIO.setup(PUL, GPIO.IN)
	time.sleep(0.00005)


print("HALF CYCLE")


for i in range(6400):
	GPIO.setup(DIR, GPIO.IN)
	GPIO.setup(PUL, GPIO.OUT)
	# GPIO.output(ENA, GPIO.HIGH)
	# GPIO.output(PUL, GPIO.HIGH)
	time.sleep(0.00005)
	GPIO.setup(PUL, GPIO.IN)
	time.sleep(0.00005)

print("DONE")
