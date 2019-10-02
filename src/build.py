import os
import platform
import getpass
import my_compile   as comp

os_list = ["Windows","Linux","Darwin"]

if platform.system() == os_list[0]:
    pass
elif platform.system() == os_list[1]:
    username = getpass.getuser()
    dir = "/home/"+username+"/Arduino/myapp"
elif platform.system() == os_list[2]:
    username = getpass.getuser()
    print(username)

def builder(setup_list,code_list):
    if not os.path.exists(dir):
        os.makedirs(dir)

    path = dir + "/myapp.ino"

    f = open(path,'w')

    f.write("void setup(){\n")
    f.writelines(setup_list)
    f.write("}\n\n")

    f.write("void loop(){\n")
    f.writelines(code_list)
    f.write("}")

def call_compiler():
    comp.uno_compiiler(dir)
