from flask import Flask

app = Flask(__name__)

@app.route('/api/getstatus', methods=['GET'])
def get_status():
    return "The api is working"

if __name__ == '__main__':
    app.run(debug=True)