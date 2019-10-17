from kivy.app import App
from kivy.lang import Builder
from kivy.config import Config
from kivy.uix.label import Label
from kivy.uix.widget import Widget
from kivy.uix.button import Button
from kivy.uix.slider import Slider
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput
from kivy.uix.gridlayout import GridLayout
from kivy.uix.screenmanager import ScreenManager,Screen,NoTransition,SlideTransition
from kivy.properties import ObjectProperty,ListProperty,StringProperty,NumericProperty,OptionProperty

path = "kv/property.kv"
Builder.load_file(path)
Config.set("graphics","resizable",True)
Config.set("graphics","width",1280)
Config.set("graphics","height",720)
#Config.set('graphics', 'window_state', 'maximized')





import os
import copy
import build as core

class Coder_t(Screen):
    def __init__(self,**kwargs):
        super(Coder_t,self).__init__(**kwargs)
        pass
    
    all = ListProperty([])
    buf = ListProperty([])
    console = ObjectProperty(None)
    slider = ObjectProperty(None)
    sl_btn = ObjectProperty(None)

    traffic1 = ObjectProperty(None)
    traffic2 = ObjectProperty(None)
    traffic3 = ObjectProperty(None)

    state_flag = []
    state_buffer = []                  #None = 0,B_ON/OFF = 1/2 ...

    setup = ["\tpinMode(2,OUTPUT);\n","\tpinMode(3,OUTPUT);\n","\tpinMode(4,OUTPUT);\n"]
    command_list = []
    command_buffer = []

    count = count_buffer = 1

    reset_flag = False
    button_pattern = []

    def printcsl(self,arg):
        if self.count < 10:
            data = str(self.count) + ".    " + arg
        elif 10 <= self.count & self.count <100:
            data = str(self.count) + ".  " + arg
        else:
            data = str(self.count) + "." + arg

        self.all.append(data)
        self.buf = copy.copy(self.all)

        self.console.text = "\n".join(self.all) + "\n"
        
        self.count += 1
        self.count_buffer = self.count

    def event_slider(self,*arg):
        self.sl_btn.text = str('{:.0f}'.format(int(self.slider.value))) + " sec waiting"
        pass
    
    def set_transition(self):
        self.manager.transition = SlideTransition()
        self.manager.transition.duration = 0.6
        self.manager.transition.direction = "down"

    def build(self,*arg):
        core.builder(self.setup,self.command_list)
        #core.call_compiler()

    def event_btn(self,state,id):#--test

        if state == "down" and id == 1:
            self.state_flag.append(1)
            self.command_list.append("\tdigitalWrite(2,HIGH);\n")
            self.command_buffer = copy.deepcopy(self.command_list)
            self.printcsl("Blue LED ON")
        elif state == "down" and id == 2:
            self.state_flag.append(2)
            self.command_list.append("\tdigitalWrite(3,HIGH);\n")
            self.command_buffer = copy.deepcopy(self.command_list)

            self.printcsl("Yelow LED ON")
        elif state == "down" and id == 3:
            self.state_flag.append(3)
            self.command_list.append("\tdigitalWrite(4,HIGH);\n")
            self.command_buffer = copy.deepcopy(self.command_list)

            self.printcsl("Red LED ON")
        if state == "normal" and id == 1:
            self.state_flag.append(4)
            self.command_list.append("\tdigitalWrite(2,LOW);\n")
            self.command_buffer = copy.deepcopy(self.command_list)

            self.printcsl("Blue LED OFF")
        elif state == "normal" and id == 2:
            self.state_flag.append(5)
            self.command_list.append("\tdigitalWrite(3,LOW);\n")
            self.command_buffer = copy.deepcopy(self.command_list)

            self.printcsl("Yelow LED OFF")
        elif state == "normal" and id == 3:
            self.state_flag.append(6)
            self.command_list.append("\tdigitalWrite(4,LOW);\n")
            self.command_buffer = copy.deepcopy(self.command_list)

            self.printcsl("Red LED OFF")

        self.state_buffer = copy.deepcopy(self.state_flag)
        
        print(state)
        print(self.state_flag)
        print(self.count)


    def reset(self):
        self.command_list.clear()
        self.all.clear()
        self.button_pattern.clear()

        print(self.traffic1.state,self.traffic2.state,self.traffic3.state)
        self.button_pattern.append(self.traffic1.state)
        self.button_pattern.append(self.traffic2.state)
        self.button_pattern.append(self.traffic3.state)
        self.traffic1.state = "normal"
        self.traffic2.state = "normal"
        self.traffic3.state = "normal"
        self.state_flag.clear()
        self.count = 1
        self.console.text = ""
        self.reset_flag = True
        

    def slbtn(self,value,text):
        self.printcsl(text)
        print("sl",self.state_flag,self.count)
        self.state_flag.append(0)
        self.command_list.append("\tdelay("+str(value)+"000);\n")
        self.command_buffer = copy.deepcopy(self.command_list)   
        self.state_buffer = copy.deepcopy(self.state_flag)



    def replace(self):
        
            
        self.state_flag = copy.deepcopy(self.state_buffer)

        self.command_list = copy.deepcopy(self.command_buffer)

        self.all = copy.copy(self.buf)

        self.count = self.count_buffer

        if self.reset_flag:
            self.traffic1.state = self.button_pattern[0]
            self.traffic2.state = self.button_pattern[1]
            self.traffic3.state = self.button_pattern[2]
            self.reset_flag = False
        elif not self.command_list and not self.reset_flag:
            return
        else:
            if self.state_flag[self.count-2]  == 4:
                self.traffic1.state = "normal"
            if self.state_flag[self.count-2]  == 5:
                self.traffic2.state = "normal"
            if self.state_flag[self.count-2]  == 6:
                self.traffic3.state = "normal"
            if self.state_flag[self.count-2]  == 1:
                self.traffic1.state = "down"
            if self.state_flag[self.count-2]  == 2:
                self.traffic2.state = "down"
            if self.state_flag[self.count-2]  == 3:
                self.traffic3.state = "down"



        
        self.console.text = ""
        self.console.text = "\n".join(self.all) + "\n"

        print(self.state_flag,self.count)
        

    def delete(self):
        if not self.command_list:
            return

        print(self.state_flag)
        print(self.count)

        if self.state_flag[self.count-2]  == 1:
            self.traffic1.state = "normal"
        if self.state_flag[self.count-2]  == 2:
            self.traffic2.state = "normal"
        if self.state_flag[self.count-2]  == 3:
            self.traffic3.state = "normal"
        if self.state_flag[self.count-2]  == 4:
            self.traffic1.state = "down"
        if self.state_flag[self.count-2]  == 5:
            self.traffic2.state = "down"
        if self.state_flag[self.count-2]  == 6:
            self.traffic3.state = "down"    
      
        self.state_buffer = copy.deepcopy(self.state_flag)

        self.command_buffer = copy.deepcopy(self.command_list)
        self.buf = copy.copy(self.all)
        self.count_buffer = self.count

        self.state_flag.pop()
        self.command_list.pop()
        self.all.pop()
        self.count -= 1

        self.console.text = ""
        self.console.text = "\n".join(self.all) + "\n"

        

        


        
        
class Simulator(Screen):
    def __init__(self,**kwargs):
        super(Simulator,self).__init__(**kwargs)
        pass



class Slide(Screen):
    source = StringProperty("")

    image = ObjectProperty(None)
    next_btn = ObjectProperty(None)
    num_of_pages = ObjectProperty(None)

    directory = ""
    pages = 0

    def __init__(self,dir_name = "./image",**kwargs):
        super(Slide,self).__init__(**kwargs)
        self.directory = dir_name
        self.get_filepath(self.directory)
        self.source = os.path.join(self.directory,self.filepath[0])
        pass

    def get_filepath(self,dir_name):
        self.filepath = os.listdir(self.directory)

    def next(self,*arg):
        self.pages += 1

        if self.pages == len(self.filepath):
            self.manager.transition.direction = "down"
            self.manager.current = "coder"
            self.pages = 0
            self.source = os.path.join(self.directory,self.filepath[self.pages])
            self.image.reload()
            self.num_of_pages.text = str(int(self.pages + 1))+" page"
            pass

        self.source = os.path.join(self.directory,self.filepath[self.pages])
        self.image.reload()
        self.num_of_pages.text = str(int(self.pages + 1))+" page"

    def back(self,*arg):
        if self.pages == 0:
            return
        self.pages -= 1 
        
        self.source = os.path.join(self.directory,self.filepath[self.pages])
        self.image.reload()
        self.num_of_pages.text = str(int(self.pages + 1))+" page"

    def change_text(self):
        if self.pages == len(self.filepath)-1:
            self.next_btn.text = "END"
        else:
            self.next_btn.text = "next"

    

class Select(Screen):

    tr_btn = ObjectProperty(None)

    def __init__(self,**kwargs):
        super(Select,self).__init__(**kwargs)

    def set_screen(self):
        if self.tr_btn.text == "traffic":
            self.coder = Coder_t(name = "coder")
            self.slide = Slide(name = "slide",dir_name = "./image")
        


class MainApp(App):
    def __init__(self,**kwargs):
        super(MainApp,self).__init__(**kwargs)
        self.title = 'MuffinTime'
        self.use_kivy_settings = False
    
    def build(self):            #make widget tree and associate kivy
        self.sm = ScreenManager()        
        self.sm.add_widget(Select(name = "select"))
        self.sm.add_widget(Simulator(name = "simulator"))
        return self.sm
        

if __name__ == '__main__':
    
    MainApp().run()
