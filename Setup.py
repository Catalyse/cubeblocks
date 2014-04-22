import sys
from cx_Freeze import setup, Executable

setup(
    name = "CubeBlocks Modifier - v0.5b by Catalyse",
    version = "0.5b",
    description = "Modifies the Time Frames of your CubeBlocks File",
    executables = [Executable("X:\workspace\Cubeblocks\src\Main.py", base = "Console")])
