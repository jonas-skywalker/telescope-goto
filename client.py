import socket
import sys
import time
import RPi.GPIO as GPIO

PUL = 18
ENA = 23
DIR = 15

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
s = socket.socket()
port = 1234
s.bind(('', port))


GPIO.setup(PUL, GPIO.OUT)
#GPIO.setup(ENA, GPIO.OUT)
GPIO.setup(DIR, GPIO.OUT)


def movesteplr(isleft, isright):
  if isleft and not isright:
    GPIO.setup(DIR, GPIO.OUT)
  if isright and not isleft:
    GPIO.setup(DIR, GPIO.IN)
  if isleft or isright:
    for i in range(100):
      print("MOVE")
      GPIO.setup(PUL, GPIO.IN)
      time.sleep(0.00005)
      GPIO.setup(PUL, GPIO.OUT)
      time.sleep(0.00005)


def receive_command():
  print("Looking for a connection...")
  #GPIO.setup(18, GPIO.OUT)
  s.listen(5)
  conn, addr = s.accept()
  #on = True
  left = False
  right = False
  up = False
  down = False
  print('Connected by', addr)
  while True:
    #print(up, down, left, right)
    if left:
      #GPIO.output(18, GPIO.HIGH)
      print('LEFT')
    elif right:
      #GPIO.output(18, GPIO.HIGH)
      print('RIGHT')
    elif up:
      #GPIO.output(18, GPIO.HIGH)
      print('UP')
    elif down:
      #GPIO.output(18, GPIO.LOW)
      print('DOWN')
    
    movesteplr(left, right)
    
    try:
      rcvdData = conn.recv(1024).decode()
      data = rcvdData.strip('\n')
      print(data)
    except:
      print("Lost Connection...")
      break
    if not rcvdData:
      break

    if data == "LEFT":
      left = True
      right = False
      up = False
      down = False
    elif data == "RIGHT":
      left = False
      right = True
      up = False
      down = False
    elif data == "UP":
      left = False
      right = False
      up = True
      down = False
    elif data == "DOWN":
      left = False
      right = False
      up = False
      down = True
    else:
      left = False
      right = False
      up = False
      down = False

  print("Closing socket...")
  GPIO.setup(PUL, GPIO.IN)
  #GPIO.setup(ENA, GPIO.OUT)
  GPIO.setup(DIR, GPIO.IN)


while 1:
	receive_command()
