import sys
from flask import Flask, jsonify, request, render_template
from flask_cors import cross_origin
from urllib.parse import urlparse
import time
import serial
import json
import SerialHandler
from threading import Thread

app = Flask(__name__)


def startServer():
    app.run(host='127.0.0.1', port=5001)


def listen():
    while 1:
        try:
            start = time.time()
            response = ser2.readline().decode(errors="replace")
            # response = ser1.readline().decode(errors="replace") # use this for running on pi
            programData = json.loads(response)
            return programData
        except Exception as e:
            pass


def echo():
    # request to get program data from windows
    jason = [{"Name": "WindowsVolumeMixerControl", "Funcs": [
        {"Name": "getAllSoundDeviceData", "Params": ["1", "2"]}]}]
    output = (json.dumps(jason) + '\n').encode()
    ser1.write(output)


@app.route('/data2')
def hello():
    return jsonify(listen())


@app.route("/data")
def data():

    content = request.args
    name = request.args.get('Name')
    funcs = request.args.get('Func')
    params = request.args.get("Params")
    processId = request.args.get("ProcessId")

    jason = [{"Name": name, "Funcs": [
        {"Name": funcs, "Params": [params, processId]}]}]

    output = (json.dumps(jason) + '\n').encode()
    ser1.write(output)

    return jsonify(request.args)


if __name__ == "__main__":
    print('starting server')
    ser1 = serial.Serial(
        port='COM4',  # for emulation insert your COMX port here
        # port='/dev/ttys0', # for use on the pi
        baudrate=20000,
        parity=serial.PARITY_NONE,
        stopbits=serial.STOPBITS_ONE,
        bytesize=serial.EIGHTBITS,
        timeout=1
    )

    # comment this out when running on the pi
    ser2 = serial.Serial(
        port='COM6',
        baudrate=20000,
        parity=serial.PARITY_NONE,
        stopbits=serial.STOPBITS_ONE,
        bytesize=serial.EIGHTBITS,
        timeout=1
    )
    # Thread(target = listen).start() # do not uncomment this bruh
    Thread(target=startServer).start()
    Thread(target=echo).start()
