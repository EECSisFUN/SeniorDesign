import serial.tools.list_ports


def checkConnected(port):
    ports = list(serial.tools.list_ports.comports())
    for p in ports:
        if p.device == port:
            return True
    return False