import sys
from flask import Flask, render_template, request, redirect, Response
from steer import computeAngles, moveAngle, readMotors

app = Flask(__name__)
@app.route('/')
def index():
    return render_template('index.html')
def testf():
	return u'testf hi'
@app.route('/receiver', methods = ['POST'])
def replyfunc():
    jsonData = request.get_json()
    print(jsonData)
    print(request)
    ang = request.form.get('angle')
    speed = request.form.get('speed')
    moveAngle(int(ang),int(speed),0)
    retjson = readMotors();
    return retjson


app.jinja_env.globals.update(testf=testf) 

if __name__ == '__main__':

    app.run(debug=True, host='0.0.0.0')