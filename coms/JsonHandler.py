from Apps import SpotifyControl
from Apps import WindowsVolumeMixerControl
from Apps import WindowsProgramControl
from Apps import ExampleApp
from Apps import Drawing
from Apps import LaunchApplication
from Apps import Twitch
import time
import SerialHandler

# JsonHandler.py
# this file handles function calls that come from the device and their return

def setupApps():
    # some apps will require startup methods to init certain things
    SpotifyControl.setup()
    WindowsVolumeMixerControl.updateDevices()
    WindowsProgramControl.setup()
    LaunchApplication.setup()
    Twitch.setup()


def callFunctions(json):
    # parses the json from the device and calls appropriate functions e.g. change master volume
    for i in json:
        for f in i["Funcs"]:
            try:
                # this lines finds a function in a module matching the function string given by the json and calls it
                return getattr(globals()[i["Name"]], f["Name"])(*f["Params"])
            except Exception as e:
                print(e)
                return None

