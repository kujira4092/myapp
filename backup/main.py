from kivy.config import Config
Config.set("graphics","resizable",True)
Config.set("graphics","width",1280)
Config.set("graphics","height",720)
import kivy
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.properties import ObjectProperty,ListProperty
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.slider import Slider
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager,Screen

codes = []
buf0 = []
buf1 = []
lists = []


class Traffic(BoxLayout):
    root = BoxLayout()
    def __init__(self,**kwargs):
        super(Traffic,self).__init__(**kwargs)


        #result view tree
        self.root.view = BoxLayout(size_hint_x = 3.5,orientation = "vertical")
        view = self.root.view
        view.console = TextInput(readonly = True,size_hint_y = 6.5,text = "")
        view.input = TextInput(multiline = False,size_hint_y = 0.5)
        view.input.bind(on_text_validate = self.ev_sendmsg)
        #associate with "view"
        view.add_widget(view.console)
        view.add_widget(view.input)



        #GUI's tree
        self.root.gui = BoxLayout(size_hint_x = 6.5,orientation = "vertical")
        gui = self.root.gui
        #make UI--button
        btn = gui.buttonBox = GridLayout(size_hint_y = 2.5,cols = 4,rows = 2,spacing = 12,padding = 15)
        btn.oprate1 = Button(text = "blue")
        btn.oprate2 = Button(text = "red")
        btn.oprate3 = Button(text = "yelow")
        btn.oprate4 = Button(text = "wait")
        btn.oprate5 = Button(text = "blue")
        btn.oprate6 = Button(text = "red")
        btn.oprate7 = Button(text = "yelow")
        btn.oprate8 = Button(text = "wait")

        btn.oprate1.bind(on_press = self.ev_pushbtn)
        btn.oprate2.bind(on_press = self.ev_pushbtn)
        btn.oprate3.bind(on_press = self.ev_pushbtn)

        btn.add_widget(btn.oprate1)
        btn.add_widget(btn.oprate2)
        btn.add_widget(btn.oprate3)
        btn.add_widget(btn.oprate4)
        btn.add_widget(btn.oprate5)
        btn.add_widget(btn.oprate6)
        btn.add_widget(btn.oprate7)
        btn.add_widget(btn.oprate8)

        #make UI--slider
        sl = gui.sliderBox = BoxLayout(size_hint_y = 2)
        sl.enpty =Label(size_hint_x = 0.5)
        sl.slider = Slider(size_hint_x = 7,min = 0,max = 100,value = 25)
        sl.slider.bind(on_touch_move = self.ev_slider,on_touch_up = self.ev_slider)
        
        sl.box = BoxLayout(size_hint_x = 2.5,padding = (30,50,30,50))
        sl.button = Button(text = format(sl.slider.value))
        sl.button.bind(on_press = self.btnev_sendmsg)
        sl.box.add_widget(sl.button)

        sl.add_widget(sl.enpty)
        sl.add_widget(sl.slider)
        sl.add_widget(sl.box)

        gui.enpty = Label(size_hint_y = 4,text = "test")

        oprate = gui.opbutton = BoxLayout(size_hint_y = 1.5,padding = 15,orientation = "horizontal")
        oprate.enpty = Label()
        oprate.undo = Button(text = "UNDO")
        oprate.reset = Button(text = "RESET")
        oprate.run = Button(text = "RUN")

        oprate.reset.bind(on_press = self.ev_pushbtn)
        oprate.undo.bind(on_press = self.ev_pushbtn)

        oprate.add_widget(oprate.enpty)
        oprate.add_widget(oprate.undo)
        oprate.add_widget(oprate.reset)
        oprate.add_widget(oprate.run)

        #To gui add any tree
        gui.add_widget(gui.buttonBox)
        gui.add_widget(gui.sliderBox)
        gui.add_widget(gui.enpty)
        gui.add_widget(gui.opbutton)

        #associate with root
        self.root.add_widget(gui)
        self.root.add_widget(view)

    all = ListProperty()
    def ev_sendmsg(self,str):
        data = str.text
        self.all.append(data)
        self.root.view.console.text = "\n".join(self.all)
        self.root.view.input.text=""
        pass

    def btnev_sendmsg(self,input):
        data = input.text
        self.all.append(data)
        self.root.view.console.text = "\n".join(self.all)
        self.root.view.input.text=""
        pass
    
    def ev_slider(self,*arg):
        self.root.gui.sliderBox.button.text = str(int(self.root.gui.sliderBox.slider.value))

    def ev_pushbtn(self,str):
        global lists,buf0,buf1
        if str.text == "blue":
            buf0 = lists.copy()
            lists.append(0)
            print(lists)
        elif str.text == "red":
            buf0 = lists.copy()
            lists.append(1)
            print(lists)
        elif str.text == "yelow":
            buf0 = lists.copy()
            lists.append(2)
            print(lists)
        elif str.text == "RESET":
            buf0 = lists.copy()
            lists.clear()
            print(lists,buf0)
        elif str.text == "UNDO":
            buf1 = buf0.copy()
            buf0 = lists.copy() 
            lists = buf1.copy()
            print(lists,buf0)
        


    
class MainApp(App):
    def __init__(self,**kwargs):
        super(MainApp,self).__init__(**kwargs)
        self.title = 'MuffinTime'
        self.use_kivy_settings = False
    
    def build(self):            #make widget tree and associate kivy
        test = Traffic()
        root = BoxLayout()
        root.add_widget(test.root)
        return root

if __name__ == '__main__':
    MainApp().run()