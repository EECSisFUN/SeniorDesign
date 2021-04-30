'''
Ref: https://stackoverflow.com/questions/53132434/list-of-installed-programs/54825112
     https://stackoverflow.com/questions/32341661/getting-a-windows-program-icon-and-saving-it-as-a-png-python/39811146
'''
import copy
import glob
import os
import re
import winreg

import win32api
import win32con
import win32gui
import win32ui
import winshell
from PIL import Image
from pywinauto import Desktop
from pywinauto import warnings
from pywinauto.application import Application
import json
from Apps import ImageWriter

app = None
windows = None


def setup():
    global app
    global windows
    app = Application()
    windows = Desktop(backend="uia").windows()
    warnings.simplefilter('ignore', category=UserWarning)


def foo(hive, flag):
    aReg = winreg.ConnectRegistry(None, hive)
    aKey = winreg.OpenKey(aReg, r"SOFTWARE\Microsoft\Windows\CurrentVersion\Uninstall", 0, winreg.KEY_READ | flag)

    count_subkey = winreg.QueryInfoKey(aKey)[0]

    software_list = []

    for i in range(count_subkey):
        software = {}
        try:
            asubkey_name = winreg.EnumKey(aKey, i)
            asubkey = winreg.OpenKey(aKey, asubkey_name)
            software['name'] = winreg.QueryValueEx(asubkey, "DisplayName")[0]

            if winreg.QueryValueEx(asubkey, "InstallLocation")[0]:
                software['install_location'] = winreg.QueryValueEx(asubkey, "InstallLocation")[0]
            else:
                software['install_location'] = 'undefined'
            software_list.append(software)
        except EnvironmentError:
            continue

    return software_list


def getInstalledApps():
    apps = foo(winreg.HKEY_LOCAL_MACHINE, winreg.KEY_WOW64_32KEY) + foo(winreg.HKEY_LOCAL_MACHINE,
                                                                        winreg.KEY_WOW64_64KEY) + foo(
        winreg.HKEY_CURRENT_USER, 1)

    for app in apps:
        for key, value in list(app.items()):
            if value == 'undefined':
                app.clear()
    apps = list(filter(None, apps))
    return apps


def launchApp(path):
    global app
    try:
        app = app.connect(path=path)
    except Exception as e:
        try:
            app = Application().start(path)
        except Exception as ex:
            print(ex)


def extractFileNames(directory):
    from os import listdir
    from os.path import isfile, join
    files = [f for f in listdir(directory) if isfile(join(directory, f))]

    program_names = []
    if files:
        for f in files:
            f_copy = copy.copy(f)
            r = re.compile('\.lnk$')
            if r.search(f_copy):
                f_copy = f_copy.replace('.lnk', '')
                # if not "Uninstall" in f_copy \
                #         and not "uninstall" in f_copy \
                #         and not "remove" in f_copy \
                #         and not "Remove" in f_copy \
                #         and not "x86" in f_copy \
                #         and not "Telemetry" in f_copy \
                #         and not "preferences" in f_copy \
                #         and not "skinned" in f_copy:
                program_names.append(f_copy.replace(" ", "_"))
    return program_names


def fetchExePaths(directory):
    exePaths = []
    for lnk in glob.glob(os.path.join(directory, "*.lnk")):
        shortcut = winshell.shortcut(lnk)
        # print(shortcut.lnk_filepath)
        # if not "Uninstall" in shortcut.lnk_filepath \
        #         and not "uninstall" in shortcut.lnk_filepath \
        #         and not "remove" in shortcut.lnk_filepath \
        #         and not "Remove" in shortcut.lnk_filepath \
        #         and not "x86" in shortcut.lnk_filepath \
        #         and not "Telemetry" in shortcut.lnk_filepath \
        #         and not "preferences" in shortcut.lnk_filepath \
        #         and not "skinned" in shortcut.lnk_filepath:
        if shortcut.path:
            if "VALORANT" in shortcut.lnk_filepath:
                exePaths.append(shortcut.path.replace("\\", "/") + ' --launch-product=valorant --launch-patchline=live')
            elif "Update.exe" in shortcut.path:
                app_name = str(os.path.basename(os.path.dirname(shortcut.path))) + '.exe'
                exePaths.append(shortcut.path.replace("\\", "/") + ' --processStart ' + '\"' + app_name + '\"')
            else:
                exePaths.append(shortcut.path.replace("\\", "/"))
    return exePaths


def extractExeIcons(exePath, exeName):
    # desktop = os.path.join(os.environ['USERPROFILE'], "Desktop")
    iconPath = os.getcwd() + r'\icons'
    if not os.path.exists(iconPath):
        os.mkdir(iconPath)

    try:
        path = exePath.replace("\\", "/")
        if "Discord" in path:
            path = os.environ['USERPROFILE'].replace("\\", "/") + "/AppData/Local/Discord/app.ico"
        if "valorant" in path:
            path = os.environ['systemdrive'].replace("\\",
                                                     "/") + "/ProgramData/Riot Games/Metadata/valorant.live/valorant.live.ico"
        if "Teams" in path:
            path = os.environ['USERPROFILE'].replace("\\", "/") + "/AppData/Local/Microsoft/Teams/app.ico"
        icoX = win32api.GetSystemMetrics(win32con.SM_CXICON)
        icoY = win32api.GetSystemMetrics(win32con.SM_CYICON)

        large, small = win32gui.ExtractIconEx(path, 0)
        win32gui.DestroyIcon(small[0])

        hdc = win32ui.CreateDCFromHandle(win32gui.GetDC(0))
        hbmp = win32ui.CreateBitmap()
        hbmp.CreateCompatibleBitmap(hdc, icoX, icoY)
        hdc = hdc.CreateCompatibleDC()

        hdc.SelectObject(hbmp)
        hdc.DrawIcon((0, 0), large[0])

        bmpstr = hbmp.GetBitmapBits(True)
        img = Image.frombuffer(
            'RGBA',
            (32, 32),
            bmpstr, 'raw', 'BGRA', 0, 1
        )

        new_img_location = iconPath + '\\' + exeName + '.ico'
        img.save(new_img_location, format("ico"))
        new_img_location = new_img_location.replace("\\", "/")

        hbmp.SaveBitmapFile(hdc, iconPath + '\\' + exeName + '.bmp')
    except:
        new_img_location = None
    return new_img_location


def verifyExeIcons(iconPath):
    if iconPath is None:
        return iconPath
    img_size = os.path.getsize(iconPath)
    path = iconPath
    if img_size < 1999:
        path = iconPath[:len(iconPath) - 3] + 'bmp'
    return path


def createProgramInfo(list1, list2, list3):
    programs = []
    for a, b, c in zip(list1, list2, list3):
        program = {'name': a, 'exe_path': b, 'icon_path': c}
        programs.append(program)
    return programs


def traverseSubdirectories(cur_directory):
    all_programs = []
    all_directories = [x[0] for x in os.walk(cur_directory)]

    for dir in all_directories:
        exe_paths = fetchExePaths(dir)
        exe_names = extractFileNames(dir)

        icon_paths = []
        for path, name in zip(exe_paths, exe_names):
            icon = extractExeIcons(path, name)
            icon_paths.append(icon)

        all_programs.append(createProgramInfo(exe_names, exe_paths, icon_paths))
    return all_programs


def launchApp(exe_file):
    try:
        os.startfile(exe_file)
    except Exception:
        import subprocess
        subprocess.Popen(exe_file)


def getAllApplicationsEmulation():
    system_progs = traverseSubdirectories(r'C:\ProgramData\Microsoft\Windows\Start Menu\Programs')
    user_progs = traverseSubdirectories(winshell.programs())
    all_programs = system_progs + user_progs

    # flatten 2D array to 1D array
    from functools import reduce
    all_programs_list = reduce(lambda x, y: x + y, all_programs)

    # do a check here for icons since some of them dont show up as ico files
    # instead replacing them bitmaps that dont have transparent background
    for prog in all_programs_list:
        prog['icon_path'] = verifyExeIcons(prog['icon_path'])

    # print(json.dumps(all_programs_list, separators=(',', ':'), indent = 1))
    return json.dumps(all_programs_list, separators=(',', ':'))


def getAllApplicationsRPi():
    system_progs = traverseSubdirectories(r'C:\ProgramData\Microsoft\Windows\Start Menu\Programs')
    user_progs = traverseSubdirectories(winshell.programs())
    all_programs = system_progs + user_progs

    # flatten 2D array to 1D array
    from functools import reduce
    all_programs_list = reduce(lambda x, y: x + y, all_programs)

    all_programs_list_rpi = []

    for prog in all_programs_list:
        try:
            if prog['icon_path'] is not None:
                string = ImageWriter.iconTo64String(prog['icon_path'])
                jason = {"name": prog['name'],
                         "exe_path": prog['exe_path'],
                         "icon_path": string}

                all_programs_list_rpi.append(jason)
        except:
            pass
    return json.dumps(all_programs_list_rpi, separators=(',', ':'))


def setup():
    getAllApplicationsEmulation()
    getAllApplicationsRPi()