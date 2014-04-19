import sys
from cx_Freeze import setup, Executable

setup(
    name = "CubeBlocks Modifier",
    version = "0.1",
    description = "Modifys the Time Frames of your CubeBlocks File",
    executables = [Executable("X:\workspace\Cubeblocks\src\Main.py", base = "Console")])
