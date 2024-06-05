import os
import platform

def clear():
	if platform.system() == "Linux":
		os.system("clear")
	else:
		os.system("cls")