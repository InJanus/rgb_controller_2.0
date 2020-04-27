from flask import Flask
from flask_cors import CORS
import RPi.GPIO as GPIO

app = Flask(__name__)
CORS(app)
GPIO.setmode(GPIO.BOARD)

@app.route('/api/getstatus', methods=['GET'])
def get_status():
    return "The api is working"

if __name__ == '__main__':
    GPIO.setup(12, GPIO.OUT) # red
    # GPIO.setup(13, GPIO.OUT) # green
    # GPIO.setup(19, GPIO.OUT) # blue
    red = GPIO.PWM(12, 1000)
    # green = GPIO.PWM(13, 1000)
    # blue = GPIO.PWM(19, 1000)
    red.start(50)
    # blue.start(50)
    # green.start(50)
    app.run(debug=True)