from flask import Flask, render_template, request, redirect, url_for
import threading

import PiMotor
# from PiMotor import Sensor

m1 = PiMotor.Motor("MOTOR1",1)
m2 = PiMotor.Motor("MOTOR2",1)
m3 = PiMotor.Motor("MOTOR3",1)
m4 = PiMotor.Motor("MOTOR4",1)

# us=Sensor("ULTRASONIC",120)
# irFront=Sensor("IR2",1)
# irBack=Sensor("IR1",1)

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
   leftMotors.reverse(80)

def turnRight():
   rightMotors.reverse(80)
   leftMotors.forward(80)

def stop():
   motorAll.stop()

def obstacleAvoidanceMode():
   obstacleAvoidanceMode()

def sumoBotMode():
   sumoBotMode()

@app.route("/<action1>")
def action1(action1):
   # Convert the pin from the URL into an integer:
   global message
   if action1 == "forward":
      message = "forward"
      thread = threading.Thread(target=forward)
      thread.start()
      return message + ' started' 
   elif action1 == "reverse":
      message = "reverse"
      thread = threading.Thread(target=reverse)
      thread.start()
      return message + ' started' 
   elif action1 == "turnLeft":
      message = "turnLeft"
      thread = threading.Thread(target=turnLeft)
      thread.start()
      return message + ' started' 
   elif action1 == "turnRight":
      message = "turnRight"
      thread = threading.Thread(target=turnRight)
      thread.start()
      return message + ' started' 
   elif action1 == "stop":
      message = "stop"
      thread = threading.Thread(target=stop)
      thread.start()
      return message + ' started' 
   elif action1 == "obstacleAvoidanceMode":
      message = "obstacleAvoidanceMode"
      thread = threading.Thread(target=obstacleAvoidanceMode)
      thread.start()
      return message + ' started' 
   elif action1 == "sumoBotMode":
      message = "sumoBotMode"
      thread = threading.Thread(target=sumoBotMode)
      thread.start()
      return message + ' started' 
   else:
      message = ""

   templateData = {
      'message' : message,
   }

if __name__ == "__main__":
   app.run(host='0.0.0.0', port=80, debug=True)

def obstacleAvoidanceMode():
   print("Obstacle Avoidance code missing")

def sumoBotMode():
   print("sumo bot code missing")


