from flask import Flask, render_template, request, redirect, url_for
import threading

import PiMotor
# from PiMotor import Sensor

m1 = PiMotor.Motor("MOTOR1",1)
m2 = PiMotor.Motor("MOTOR2",1)
m3 = PiMotor.Motor("MOTOR3",1)
m4 = PiMotor.Motor("MOTOR4",1)

motorSpeed = 10

us=Sensor("ULTRASONIC",120)
irFrontLeft=Sensor("IR2",1)
irFrontRight=Sensor("IR3", 1)
irBack=Sensor("IR1",1)

#To drive all motors together
motorAll = PiMotor.LinkedMotors(m1,m2,m3,m4)
rightMotors = PiMotor.LinkedMotors(m1,m2)
leftMotors = PiMotor.LinkedMotors(m3,m4)

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('main.html')
   
@app.route("/")
def main():
   templateData = {
      'message': ""
      }
   # Pass the template data into the template main.html and return it to the user
   return message
  
def forward():
   motorAll.forward(100)

def reverse():
   motorAll.reverse(100)

def turnLeft():
   rightMotors.forward(80)
   leftMotors.forward(40)

def turnRight():
   rightMotors.forward(40)
   leftMotors.forward(80)

def stop():
   motorAll.stop()

def obstacleAvoidanceMode():
   obstacleAvoidanceMode()

def sumoBotMode():
   sumoBotMode()

def lineFollowingMode():
   lineFollowingMode()

@app.route("/<action1>")
def action1(action1):
   # Convert the pin from the URL into an integer:
   global message
   if action1 == "forward":
      message = "forward"
      thread = threading.Thread(target=forward)
      thread.start()
      render_template('main.html')
   elif action1 == "reverse":
      message = "reverse"
      thread = threading.Thread(target=reverse)
      thread.start()
      render_template('main.html')
   elif action1 == "turnLeft":
      message = "turnLeft"
      thread = threading.Thread(target=turnLeft)
      thread.start()
      return message + ' started' 
   elif action1 == "turnRight":
      message = "turnRight"
      thread = threading.Thread(target=turnRight)
      thread.start()
      render_template('main.html')
   elif action1 == "stop":
      message = "stop"
      thread = threading.Thread(target=stop)
      thread.start()
      render_template('main.html')
   elif action1 == "obstacleAvoidanceMode":
      message = "obstacleAvoidanceMode"
      thread = threading.Thread(target=obstacleAvoidanceMode)
      thread.start()
      render_template('main.html')
   elif action1 == "sumoBotMode":
      message = "sumoBotMode"
      thread = threading.Thread(target=sumoBotMode)
      thread.start()
      render_template('main.html') 
   elif action1 == "lineFollowingMode":
      message = "lineFollowingMode"
      thread = threading.Thread(target=lineFollowingMode)
      thread.start()
      render_template('main.html') 
   else:
      message = ""

   templateData = {
      'message' : message,
   }

if __name__ == "__main__":
   app.run(host='0.0.0.0', port=80, debug=True)

def obstacleAvoidanceMode():
   us.boundary = 15
   us.trigger()
   if us.Triggered:
      rightMotors.forward(80)
      leftMotors.reverse(80)
      time.sleep(1)
   else:
      motorAll.forward(80)
      
def sumoBotMode():
   al.on()
   ar.on()
   ab.on()
   af.on()
   print ("LA: Going to the center...")
   m1.reverse(70)
   m2.reverse(70)
   m3.reverse(100)
   m4.reverse(100)
   time.sleep(1.8)
   motorAll.stop()
   while True:
      findOpponent()

def lineFollowingMode():
   while True:
      irFrontLeft.trigger()
      irFrontRight.trigger()
      if irFrontLeft.Triggered and irFrontRight.Triggered:
         motorAll.forward(80)
         time.sleep(0.1)
      elif irFrontLeft.Triggered and not irFrontRight.Triggered:
         rightMotors.forward(80)
         leftMotors.reverse(80)
         time.sleep(0.1)
      elif not irFrontLeft.Triggered and irFrontRight.Triggered:
         leftMotors.forward(80)
         rightMotors.reverse(80)
         time.sleep(0.1)


def trigIR():
    irFrontLeft.trigger()
    irBack.trigger()
    if irFrontLeft.Triggered:
        motorAll.reverse(100)
        time.sleep(1.2)
        motorAll.stop()
        print("LA: Front Line Detected")
    if irBack.Triggered:
        motorAll.forward(100)
        time.sleep(1.2)
        motorAll.stop()
        print("LA: Back Line Detected")

def findOpponent():
    print("LA: Finding")
    print("Finding")
    trigIR()
    motorSpeed = 40
    while True:
	print("LA: ")
	print(us.lastRead)
        trigIR()
        us.boundary = 80
        us.trigger()
        time.sleep(0.001)
        motorAll.stop()
        if us.Triggered:
            print("LA: Found")
            trigIR()
            break
            
        leftMotors.forward(45)
        rightMotors.reverse(45)
        trigIR()
        time.sleep(0.000001)

    if us.Triggered:
        print("LA: Found opponent")
        count = 0
	trigIR()
	while us.Triggered and count < 2:
	    trigIR()
	    print("LA: ")
	    print(us.lastRead)
	    print("Motorspeed: ")
	    print(motorSpeed)
	    print("Count:")
	    print(count)
	    us.trigger()
	    trigIR()
	    if irFrontLeft.Triggered:
	    	count = count + 1
		if count == 2:
			leftMotors.forward(100)
			rightMotors.reverse(100)
			trigIR()
			time.sleep(0.5)
            if us.lastRead <= 7 and not irFrontLeft.Triggered and not irBack.Triggered:
                motorSpeed = 100
            else:
                motorSpeed = 30
            motorAll.forward(motorSpeed)



