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
from kivy.properties import ObjectProperty,ListProperty,StringProperty,NumericProperty

path = "kv/property.kv"
Builder.load_file(path)
Config.set("graphics","resizable",True)
Config.set("graphics","width",1280)
Config.set("graphics","height",720)
#Config.set('graphics', 'window_state', 'maximized')


traffic_setup = ["\tpinMode(2,OUTPUT);\n","\tpinMode(3,OUTPUT);\n","\tpinMode(4,OUTPUT);\n"]
traffic_code = []


import os
import threading

import build as core

class Coder(Screen):
    def __init__(self,**kwargs):
        super(Coder,self).__init__(**kwargs)
        pass
    
    all = ListProperty()

    console = ObjectProperty(None)
    slider = ObjectProperty(None)
    sl_btn = ObjectProperty(None)

    count = 0
    def printcsl(self,arg):
        if self.count < 10:
            data = str(self.count) + ".    " + arg
        elif 10 <= self.count & self.count <100:
            data = str(self.count) + ".  " + arg
        else:
            data = str(self.count) + "." + arg

        self.all.append(data)
        self.console.text = "\n".join(self.all) + "\n"
        self.count += 1

    def ev_slider(self,*arg):
        self.sl_btn.text = str(int(self.slider.value)) + "sec  waiting"
        pass
    
    def set_transition(self):
        self.manager.transition = SlideTransition()
        self.manager.transition.duration = 0.6
        self.manager.transition.direction = "down"

    def build(self,*arg):
        global traffic_code,traffic_setup
        core.builder(traffic_setup,traffic_code)
        core.call_compiler()

    def ev_btn(self,state,id):#--test
        global traffic_code
        if state == "normal":
            if id == 1:
                traffic_code.append("\tdigitalWrite(2,HIGH);\n")
                self.printcsl("!")
            elif id == 2:
                traffic_code.append("\tdigitalWrite(3,HIGH);\n")
            elif id == 3:
                traffic_code.append("\tdigitalWrite(4,HIGH);\n")
            elif id == 4:
                traffic_code.append("")
        if state == "down":
            if id == 1:
                traffic_code.append("\tdigitalWrite(2,LOW);\n")
                self.printcsl("?")
            elif id == 2:
                traffic_code.append("\tdigitalWrite(3,LOW);\n")
            elif id == 3:
                traffic_code.append("\tdigitalWrite(4,LOW);\n")
            elif id == 4:
                traffic_code.append("")
        print(state)

    def ev_reset(self):
        global traffic_code
        traffic_code.clear()

        
        
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
            self.coder = Coder(name = "coder")
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
