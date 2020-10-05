import PortsHandler
import SerialHandler
import time
from Apps import WindowsVolumeMixerControl


def main():
    running = True
    processes = WindowsVolumeMixerControl.getAllSoundDevices()
    for p in processes:
        print(p.ProcessId)
    while(running):
        print("Device Not Found")
        port = None
        port = PortsHandler.findPort()
        while(None == port):
            port = PortsHandler.findPort()
            time.sleep(10)
        print("Device has been found on port", port)
        s = SerialHandler.connectPort(port)

        while(1):
            SerialHandler.listen(s)

if __name__ == '__main__':    
    main()
