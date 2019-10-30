import subprocess
import os
import platform
import glob

board_list = ["arduino:avr:uno","arduino:avr:mega","arduino:avr:nano","arduino:avr:nano:cpu=atmega328old"]


output = str(subprocess.check_output(["arduino-cli","board","list"]))

if platform.system() == "Windows":
    pass
elif platform.system() == "Linux":
    port = glob.glob("/dev/tty[A-Za-z]*")
elif platform.system() == "Darwin":
    port = glob.glob("/dev/cu.usb*")
    


for n in range(len(board_list)):
    if output.find(board_list[n]) != -1:
        cmd = board_list[n]
        print(cmd)

path = os.path.abspath("test/myapp.ino")
print(path)

port = glob.glob("/dev/cu.usb*")
print(port)