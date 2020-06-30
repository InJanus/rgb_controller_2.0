from flask import Flask, jsonify, request
from flask_cors import CORS
import json
import pigpio

setmode = False #this is for deployment true will use the rpi.gpio class

if setmode:
    pi = pigpio.pi()

app = Flask(__name__)
CORS(app)


rpin = 19
gpin = 12
bpin = 13

rval = 0
gval = 0
bval = 0


pi.set_mode(rpin, pigpio.OUTPUT)
pi.set_mode(gpin, pigpio.OUTPUT)
pi.set_mode(bpin, pigpio.OUTPUT)

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
        pi.set_PWM_dutycycle(rpin, 255)
        pi.set_PWM_dutycycle(gpin, 255)
        pi.set_PWM_dutycycle(bpin, 255)
    else:
        print("no action since is is not a rasberry pi, did you set setmode to true?")

if __name__ == '__main__':
    app.run(debug=True)