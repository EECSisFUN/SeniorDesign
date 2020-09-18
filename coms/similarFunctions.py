import serial.tools.list_ports


def getCOMPorts():
    ports = list(serial.tools.list_ports.comports())
    raspberryPiPort = None
    emuPorts = []
    for p in ports:
        if 'Prolific USB-to-Serial Comm Port' in p.description:
            raspberryPiPort = p.device
        if 'com0com' in p.description:
            emuPorts.append(p.device)
    return raspberryPiPort, emuPorts
