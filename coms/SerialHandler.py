import serial
import json
import JsonHandler
import time


def connectPort(port):
    # the main serial connection
    return serial.Serial(
        port=port,
        baudrate=20000,
        parity=serial.PARITY_NONE,
        stopbits=serial.STOPBITS_ONE,
        bytesize=serial.EIGHTBITS,
        timeout=1)


def sendData(ser, data):
    data = (json.dumps(data) + '\n').encode()
    ser2.write(data)


def listen(ser):
    JsonHandler.updateDevices()
    while 1:
        try:
            response = ser.readline().decode(errors="replace")
            response = json.loads(response)
            # print(response)
            data = JsonHandler.callFunctions(response)
            if data != None:
                sendData(ser, data)
        except Exception as e:
            pass
