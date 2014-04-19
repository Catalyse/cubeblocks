"""
@author: Taylor May
@date: 04/18/2014
@note: Main Function for CubeBlocks Modifier
"""

import os
import shutil
import time
from xml.dom import minidom

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
    print('////////Ver-0.1b///////////  \_____\__,_|_.__/ \___|____/|_|\___/ \___|_|\_\___/ |_|  |_|\___/ \__,_|_|_| |_|\___|_|   ///////Rev-18Apr14/////////')
    print('//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////')
    return

def dirpath():
    while True:
        print()
        print("Please provide the directory of your steam installation(where Space Engineers is installed)")
        print("Example: 'C:\Program Files (x86)\Steam' for now we need the full directory!")
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
    print("You can write the ratio either way, 1/3 = .33 or 3")
    no = float(input("Please type your number here!  "))
    return no
        
def ui():
    titleScreen()
    print("This program will run and make a backup of your current file, then modify and replace the original.")
    print("There will be a copy of the original in case something goes wrong or you want to reset your times called Cubeblocks.sbc.bak")
    print()
    print("Lets begin!")
    print()
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
    for s in itemlist:
        mod = s.childNodes[0].nodeValue
        mod = int(float(mod))
        mod = mod/ratio
        mod = int(mod)
        mod = str(mod)
        s.childNodes[0].nodeValue = mod
    for s in itemlist:
        print(s.childNodes[0].nodeValue, end="")
        
    shutil.copy2(path + "\Cubeblocks.sbc", path + "\Cubeblocks.sbc.bak")
    cuberead = open(path + "\Cubeblocks.sbc.bak", "r")
    cubewrite = open(path + "\Cubeblocks.sbc", "w")
    
    i=0
    print("Loopstart")
    for line in cuberead:
        if "<BuildTimeSeconds>" in line:
            print("      <BuildTimeSeconds>"+itemlist[i].childNodes[0].nodeValue+"</BuildTimeSeconds>" + '\n', end='', file=cubewrite)
            i = i+1
            print('BuildTimeEdit', end='')
        else:
            print(line, end='', file=cubewrite)
            print("LinePost", end='')
    cubewrite.close()
    cuberead.close()
        
ui()
