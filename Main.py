"""
@author: Taylor May
@date: 04/21/2014
@note: Main Function for CubeBlocks Modifier
"""

import os
import winreg
import shutil
import time
import sys
from xml.dom import minidom

# This is d.py
import logging, logging.handlers

# Make a global logging object.
x = logging.getLogger("log")
x.setLevel(logging.DEBUG)

# This handler writes everything to a file.
h1 = logging.FileHandler("debug.log")
f = logging.Formatter("%(levelname)s %(asctime)s %(funcName)s %(lineno)d %(message)s")
h1.setFormatter(f)
h1.setLevel(logging.DEBUG)
x.addHandler(h1)

try:
    log = logging.getLogger("log")

    logfun.debug("Starting Program!")
    
    def cls():
        os.system(['clear','cls'][os.name == 'nt'])
        return
    
    def titleScreen():
        cls()
        os.system("mode con: cols=147 lines=40")
        print('//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////')
        print('/////Author:///////////////   _____      _          ____  _            _          __  __           _ _  __ _           ///////////////////////////')
        print('///////////////////////////  / ____|    | |        |  _ \| |          | |        |  \/  |         | (_)/ _(_)          ///////////////////////////')
        print('/////Catalyse////////////// | |    _   _| |__   ___| |_) | | ___   ___| | _____  | \  / | ___   __| |_| |_ _  ___ _ __ ///////////////////////////')
        print("/////////////////////////// | |   | | | | '_ \ / _ \  _ <| |/ _ \ / __| |/ / __| | |\/| |/ _ \ / _` | |  _| |/ _ \ '__|///////////////////////////")
        print('/////////////////////////// | |___| |_| | |_) |  __/ |_) | | (_) | (__|   <\__ \ | |  | | (_) | (_| | | | | |  __/ |   ///////////////////////////')
        print('////////Ver-0.5a///////////  \_____\__,_|_.__/ \___|____/|_|\___/ \___|_|\_\___/ |_|  |_|\___/ \__,_|_|_| |_|\___|_|   ///////Rev-21Apr14/////////')
        print('//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////')
        return
    
    def regget():
        try:
            registry = winreg.ConnectRegistry(None, winreg.HKEY_LOCAL_MACHINE)
            key = winreg.OpenKey(registry, "SOFTWARE\\Wow6432Node\\Microsoft\\Windows\\CurrentVersion\\Uninstall\\Steam App 244850")
            
            value = winreg.QueryValueEx(key, "InstallLocation")
            winreg.CloseKey(key)
            winreg.CloseKey(registry)
            return value[0]
        except:
            print("Error Registry entry not found!")
        finally:
            print("This program is designed for people who PURCHASED the game.  There is a 99% chance that you have pirated this game as steam installs everything in the same place every time.
            print("This game is worth buying, please help the devs!")
            time.sleep(5)
            sys.exit()
    
    def dirpath():
        value = regget()
        
        value = (value+"\Content\Data")
        
        print(value)
        
        print("Does the path above look correct?")
        print("Make sure it doesn't have extra slashes!")
        print("If it is not correct you can manually type it in after your response.")
        response = str(input("Correct? y or n:  "))
        if response == "y" or response == "Y":
            return value
        while True:
            print()
            print("Please provide the directory of your steam installation(where Space Engineers is installed)")
            print("Example: 'C:\Program Files (x86)\Steam' for now we need the full directory!")
            print()
            print("It is important to use colons : not semi-colons ; and to use brackets (), not arrows <>")
            dirpath = str(input())
            dirpath = (dirpath+"\SteamApps\common\SpaceEngineers\Content\Data")
            print(dirpath)
            print("Does the path above look correct?")
            print("Make sure it doesn't have extra slashes!")
            response = str(input("Correct? y or n:  "))
            if response == "y" or response == "Y":
                return dirpath
        
            
    def ratio():
        print("Now we need to pick the ratio at which you'd like to reduce the times")
        print("You can write the ratio either way. Eg: To cut the build time by 1/3 = .33 or 3")
        print()
        print("It is important to note that 1/3 or any fraction is NOT a valid response to this.")
        print("It MUST be a decimal or whole number")
        no = float(input("Please type your number here!  "))
        return no
            
    def ui():
        titleScreen()
        print("This program will run and make a backup of your current file, then modify and replace the original.")
        print("There will be a copy of the original in case something goes wrong or you want to reset your times called Cubeblocks.sbc.bak")
        print()
        print("Lets begin!")
        print()
        time.sleep(3)
        pa = dirpath()
        titleScreen()
        print()
        no = ratio()
        titleScreen()
        print()
        filehandler(no,pa)
        
    
    def filehandler(ratio,path):
        if ratio < 1:
            ratio = 1/ratio
        print("This program is going to print a whole bunch of statements very quickly now, this is normal and part of testing, it will be removed soon.")
        time.sleep(2)
        xmldoc = minidom.parse(path + "\Cubeblocks.sbc")
        itemlist = xmldoc.getElementsByTagName('BuildTimeSeconds') 
        print(len(itemlist))
        for s in itemlist:
            print(s.childNodes[0].nodeValue, end="")
        print()
        for s in itemlist:
            mod = s.childNodes[0].nodeValue
            mod = int(float(mod))
            mod = mod/ratio
            mod = int(mod)
            mod = str(mod)
            if(mod <.5):
                mod = .5
            s.childNodes[0].nodeValue = mod
        for s in itemlist:
            print(s.childNodes[0].nodeValue, end="")
        print()
            
        shutil.copy2(path + "\Cubeblocks.sbc", path + "\Cubeblocks.sbc.bak")
        cuberead = open(path + "\Cubeblocks.sbc.bak", "r")
        cubewrite = open(path + "\Cubeblocks.sbc", "w")
        
        l=0
        i=0
        print("Modifying your file...")
        for line in cuberead:
            if "<BuildTimeSeconds>" in line:
                print("      <BuildTimeSeconds>"+itemlist[i].childNodes[0].nodeValue+"</BuildTimeSeconds>" + '\n', end='', file=cubewrite)
                i = i+1
            else:
                print(line, end='', file=cubewrite)
        print()
        cubewrite.close()
        cuberead.close()
        print("Done!")
        time.sleep(2)
        print("GoodBye!")
        print("Press enter to close")
        input()
        sys.exit()
    ui()
except:
    logfun.exception("Well shit something broke")
    logfun.debug("Program Finished!")
