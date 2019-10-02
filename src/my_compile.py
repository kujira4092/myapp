import subprocess

def uno_compiiler(path):
    subprocess.Popen(["arduino-cli","core","update-index"])

    #subprocess.Popen(["arduino-cli","board","list"])

    subprocess.Popen(["arduino-cli","--config-file",".cli-config.yaml",
                    "compile","-b","arduino:avr:uno",path])

    subprocess.Popen(["arduino-cli","--config-file",".cli-config.yaml",
                    "upload","-p","/dev/ttyACM0","-b","arduino:avr:uno",path])
    
