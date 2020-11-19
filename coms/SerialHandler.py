import serial
import json
import JsonHandler
import time


def connectPort(port):
    # the main serial connection
    return serial.Serial(
        port='COM3',
        baudrate=115200,
        parity=serial.PARITY_NONE,
        stopbits=serial.STOPBITS_ONE,
        bytesize=serial.EIGHTBITS,
        timeout=1)

def sendData(ser, data):
    ser.flush() # flush buffer
    # comment out this whole block when using the RPi
    # ser2 = serial.Serial(
    #     port='COM3',
    #     baudrate=115200,
    #     parity=serial.PARITY_NONE,
    #     stopbits=serial.STOPBITS_ONE,
    #     bytesize=serial.EIGHTBITS,
    #     timeout=1)
    data = (json.dumps(data) + '\n').encode()
    ser.write(data)

def listen(ser):
    JsonHandler.updateDevices()
    while 1:
        try:
            response = ser.readline().decode()
            response = json.loads(response)
            print(response)
            data = JsonHandler.callFunctions(response)
            if data != None:
                sendData(ser, data)
        except Exception as e:
            pass
