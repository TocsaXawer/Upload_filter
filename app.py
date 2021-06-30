import os 
from flask import Flask, render_template, request, url_for, redirect, make_response, jsonify
import random
import json
from time import time
import psutil
app = Flask(__name__)

APP_ROOT = os.path.dirname(os.path.abspath(__file__))

@app.route("/", methods=['POST', 'GET'])
def home():
    return render_template("Main/Home/index.html")

@app.route("/Upload")
def index():
    return render_template("Upload/upload.html")

@app.route("/upload_succes", methods=['POST'])
def upload():
    
    target = os.path.join(APP_ROOT, 'UPLOAD/')
    print(target)
    

    if not os.path.isdir(target):
        os.mkdir(target)
        
    for file in request.files.getlist("file"):
        print(file)
        filename = file.filename
        destination = "/".join([target, filename])
        print(destination)
        file.save(destination)
    return render_template("Main/Home/index.html")

@app.route("/Zene")
def Zene():
	return render_template("Main/Zene/Index.html")

@app.route("/Video")
def Video():
    return render_template("Main/Video/Video.html")

@app.route("/Other")
def Other():
    return render_template("Main/Other/Index.html")

@app.route("/Documents")
def Documents():
    return render_template("Main/Documents/Index.html")

@app.route('/os.monitor', methods=["GET", "POST"])
def main():
    return render_template('Main/System/index.html')

@app.route('/os.settings', methods=["GET", "POST"])
def Setting():
    return render_template('Main/Settings/index.html')

@app.route('/data', methods=["GET", "POST"])
def data():
    # Data Format
    # [TIME, Temperature, Humidity]
    

    Temperature = psutil.cpu_percent()
    print(type(Temperature))
    svmem = psutil.virtual_memory()
    Humidity = svmem.used* 100

    data = [time() * 1000, Temperature, Humidity]

    response = make_response(json.dumps(data))

    response.content_type = 'application/json'

    return response


@app.route('/shoutdown')
def kikapcs():
    os.system('systemctl poweroff')
    return ("Kikapcs")
        
@app.route('/restart')
def restart():
    os.system('systemctl reboot')
    return("restart")










if __name__ == '__main__': app.run(host='0.0.0.0', port=4555, debug=True)
