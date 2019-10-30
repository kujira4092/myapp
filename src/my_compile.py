import subprocess
import os
import time

def setup():
    subprocess.run(["arduino-cli","--config-file",".cli-config.yaml","core","update-index"])

def compiler(path):
    subprocess.run(["arduino-cli","compile","--fqbn","arduino:avr:uno",path])


def uploader(path):
    subprocess.run(["arduino-cli","--config-file",".cli-config.yaml",
                    "upload","-p","/dev/tty.usbmodem141101","-b","arduino:avr:uno",path])
    
if __name__ == "__main__":
    setup()
    path = os.path.abspath("Arduino/")
    compiler(path)
    uploader(path)
    pass
