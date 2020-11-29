import serial
import json

def connectPort(port):
    # the main serial connection
    return serial.Serial(
        port=port,
        baudrate=115200,
        parity=serial.PARITY_NONE,
        stopbits=serial.STOPBITS_ONE,
        bytesize=serial.EIGHTBITS,
        timeout=1)


# def sendData(ser, data):
#     ser.flush()  # flush buffer
#     data = (json.dumps(data) + '\n').encode()
#     ser.write(data)


# def listen(ser1, ser2):
#     JsonHandler.updateDevices()
#     while 1:
#         try:
#             response = ser1.readline().decode()
#             response = json.loads(response)
#             print(response)
#             data = JsonHandler.callFunctions(response)
#             if data != None:
#                 sendData(ser2, data)
#         except Exception as e:
#             pass