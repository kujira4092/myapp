import os
import platform
import getpass
import my_compile   as comp

if platform.system() == "Windows":
    pass
elif platform.system() == "Linux":
    pass
elif platform.system() == "Darwin":
    path = os.path.abspath("test/myapp.ino")
    for file in os.listdir("/dev"):
        if "cu.usbmodem" in file:
            port = "/dev/" + file
            print(port)

def builder(setup_list,code_list):
    path = "test/myapp.ino"
    f = open(path,'w')

    f.write("void setup(){\n")
    f.writelines(setup_list)
    f.write("}\n\n")

    f.write("void loop(){\n")
    f.writelines(code_list)
    f.write("}")

def call_compiler():
    comp.compiler(dir)

def call_uploader():
    comp.uploader(dir)

