import serial
import json
import time

from similarFunctions import getCOMPorts


def writeSerialData():
    raspberryPiPort, emuPorts = getCOMPorts()
    if not raspberryPiPort:
        writePort = emuPorts[1]
    else:
        writePort = raspberryPiPort
    s = serial.Serial(
        port=writePort,
        baudrate=20000,
        parity=serial.PARITY_NONE,
        stopbits=serial.STOPBITS_ONE,
        bytesize=serial.EIGHTBITS,
        timeout=1)

    my_arr = [1, 2, 3, 4, 5]

    data = (json.dumps(my_arr) + '\n').encode()

    while 1:
        s.write(data)
        time.sleep(1)
