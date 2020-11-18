from Apps import WindowsVolumeMixerControl

def updateDevices():
    WindowsVolumeMixerControl.updateDevices()

# WindowsVolumeMixerControl
def WindowsVolumeMixer(funcs):
    for i in funcs:
        if(i["Name"] == "muteMasterVolume"):
            WindowsVolumeMixerControl.muteMasterVolume()
        elif(i["Name"] == "unmuteMasterVolume"):
            WindowsVolumeMixerControl.unmuteMasterVolume()
        elif(i["Name"] == "setMasterVolume"):
            WindowsVolumeMixerControl.setMasterVolume(i["Params"][0])
        elif(i["Name"] == "muteApplicationVolume"):
            WindowsVolumeMixerControl.muteApplicationVolume(i["Params"][1])
        elif(i["Name"] == "unmuteApplicationVolume"):
            WindowsVolumeMixerControl.unmuteApplicationVolume(i["Params"][1])
        elif(i["Name"] == "setApplicationVolume"):
            WindowsVolumeMixerControl.setApplicationVolume(i["Params"][1], i["Params"][0])
        elif(i["Name"] == "getAllSoundDeviceData"):
            return WindowsVolumeMixerControl.getAllSoundDeviceData()

def callFunctions(json):
    for i in json:
        if(i["Name"] == "WindowsVolumeMixerControl"):
            return WindowsVolumeMixer(i["Funcs"])


def getProcsAsJson():
    procs = WindowsVolumeMixerControl.getAllSoundDevices()
    procsJSONlist = []
    for p in procs:
        addition = {"Name": p.DisplayName, "Id": p.ProcessId}
        procsJSONlist.append(addition)
    return procsJSONlist
   