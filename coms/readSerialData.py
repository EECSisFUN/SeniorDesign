import serial
import json

from similarFunctions import getCOMPorts


def readSerialData():
    raspberryPiPort, emuPorts = getCOMPorts()
    if not raspberryPiPort:
        readPort = emuPorts[0]
    else:
        readPort = raspberryPiPort
    s = serial.Serial(
        port=readPort,
        baudrate=20000,
        parity=serial.PARITY_NONE,
        stopbits=serial.STOPBITS_ONE,
        bytesize=serial.EIGHTBITS,
        timeout=1)

    while 1:
        try:
            res = s.readline().decode(errors="replace")
            # print(res, end='')
            parsed = json.loads(res)
            print(json.dumps(parsed, indent=4, sort_keys=True))
        except:
            print("Timed out")