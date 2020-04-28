from flask import Flask, jsonify, request
from flask_cors import CORS
import json

setmode = False #this is for deployment true will use the rpi.gpio class

if setmode:
    import RPi.GPIO as GPIO
    GPIO.setmode(GPIO.BOARD)
    GPIO.setwarnings(False)

app = Flask(__name__)
CORS(app)


rpin = 19
gpin = 12
bpin = 13

rval = 0
gval = 0
bval = 0

@app.route('/api/getstatus', methods=['GET'])
def get_status():
    color = {'red': rval, 'green':gval, 'blue':bval}
    return jsonify(status=True, color=color)

@app.route('/api/color', methods=['GET','POST'])
def setColor():
    mydata = request.data.decode("utf-8")
    s = json.loads(mydata)
    rval = s['red']
    gval = s['green']
    bval = s['blue']
    activate_colors()
    return s

def activate_colors():
    if setmode:
        blue.start(50)
        green.start(50)
        red.start(50)
    else:
        print("no action since is is not a rasberry pi, did you set setmode to true?")

if __name__ == '__main__':
    if setmode:
        GPIO.setup(12, GPIO.OUT) # green
        GPIO.setup(13, GPIO.OUT) # blue
        GPIO.setup(19, GPIO.OUT) # red
        blue = GPIO.PWM(12, 1000)
        green = GPIO.PWM(13, 1000)
        red = GPIO.PWM(19, 1000)
    app.run(debug=True)