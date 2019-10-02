import kivy
from kivy.config import Config
Config.set("graphics","resizable",False)
Config.set("graphics","width",1280)
Config.set("graphics","height",720)
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.widget import Widget
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button
from kivy.uix.togglebutton import ToggleButton
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.slider import Slider
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager,Screen
from kivy.properties import ObjectProperty,ListProperty,StringProperty
from kivy.uix.image import Image
from kivy.uix.behaviors import ButtonBehavior

import os

Builder.load_file("kv/test.kv")

class MyButton (BoxLayout):
    def __init__ ( self , ** kwargs ):
        super ( MyButton , self ) . __init__ ( ** kwargs )
        pass
    
    def statef(self,status,color):
            print(status)
class mainApp(App):

    def __init__(self,**kwargs):
        super(mainApp,self).__init__(**kwargs)
        pass

    def build(self):
        return MyButton()

if __name__ == "__main__":
    mainApp().run()
    pass
