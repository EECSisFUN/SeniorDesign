from ctypes import POINTER, cast
from comtypes import CLSCTX_ALL
from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume
import re
import json

speakers = AudioUtilities.GetSpeakers()
interface = speakers.Activate(IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
volume = cast(interface, POINTER(IAudioEndpointVolume))

# Master Volume
def muteMasterVolume():
    volume.SetMute(1,None)

def unmuteMasterVolume():
    volume.SetMute(0,None)

# param: new level of volume from 0.0 to 1.0
def setMasterVolume(newVolume):
    volume.SetMasterVolumeLevelScalar(float(newVolume), None)

# Application Volume
# param: application session
def muteApplicationVolume(pid):
    devices[pid]["session"].SimpleAudioVolume.SetMute(1, None)

# param: application session
def unmuteApplicationVolume(pid):
    devices[pid]["session"].SimpleAudioVolume.SetMute(0, None)

# param: application session, and new level from 0.0 to 1.0
def setApplicationVolume(pid, newVolume):
    devices[int(pid)]["session"].SimpleAudioVolume.SetMasterVolume(float(newVolume), None)

def getAllSoundDeviceData():
    allSoundDevices = []

    procs = AudioUtilities.GetAllSessions()
    for p in procs:
        try:
            tempObject = {
                "pid": p.ProcessId,
                "name": re.split('[-.]', p.Process.name())[0].title(),
                "currentVolume": p.SimpleAudioVolume.GetMasterVolume()
            }
            allSoundDevices.append(tempObject)
        except:
            pass
    return allSoundDevices

def updateDeviceData():
    global deviceData
    deviceData = getAllSoundDeviceData()

def getAllSoundDevices():
    allSoundDevices = {}

    procs = AudioUtilities.GetAllSessions()
    for p in procs:
        try:
            tempObject = {
                "name": re.split('[-.]', p.Process.name())[0].title(),
                "currentVolume": p.SimpleAudioVolume.GetMasterVolume(),
                "session": p
            }
            allSoundDevices.update({p.ProcessId: tempObject})
        except:
            pass
    return allSoundDevices

def updateDevices():
    global devices
    devices = getAllSoundDevices()
