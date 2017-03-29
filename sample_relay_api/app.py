from flask import Flask

app = Flask(__name__)

@app.route('/control/sw<int:switchid>/1', methods=['GET'])
def switchon(switchid):
    return "Switch number: {0} is on".format(switchid)

@app.route('/control/sw<int:switchid>/0', methods=['GET'])
def switchoff(switchid):
    return "Switch number: {0} is off".format(switchid)

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)