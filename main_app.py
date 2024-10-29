from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput

from instructions import *

class UserScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        instr = Label(text= txt_instruction)

        name_label = Label(text= "Введіть ім'я")
        self.name_pac = TextInput()
        age_label = Label(text= "Введіть вік")
        self.age = TextInput()

        self.button = Button(text= "Почати")
        self.button.on_press = self.next

        layout1 = BoxLayout()
        layout1.add_widget(name_label)
        layout1.add_widget(self.name_pac)

        layout2 = BoxLayout()
        layout2.add_widget(age_label)
        layout2.add_widget(self.age)

        main_layout = BoxLayout(orientation= "vertical")
        main_layout.add_widget(instr)
        main_layout.add_widget(layout1)
        main_layout.add_widget(layout2)
        main_layout.add_widget(self.button)

        self.add_widget(main_layout)
    
    def next(self):
        self.manager.current = "pulse1"


class Pulse1Screen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        instr = Label(text= txt_test1)

        result_label = Label(text= "Введіть результати")
        self.result = TextInput()

        self.button = Button(text= "Почати")
        self.button.on_press = self.next

        layout1 = BoxLayout()
        layout1.add_widget(result_label)
        layout1.add_widget(self.result)

        main_layout = BoxLayout(orientation= "vertical")
        main_layout.add_widget(instr)
        main_layout.add_widget(layout1)
        main_layout.add_widget(self.button)

        self.add_widget(main_layout)
    
    def next(self):
        self.manager.current = "sits"


class SitsScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        instr = Label(text= txt_test2)

        self.sits = Label(text= "присідання")
        #self.runner = BoxLayout()

        self.button = Button(text= "Продовжити")
        self.button.on_press = self.next

        layout1 = BoxLayout()
        layout1.add_widget(instr)
        #layout1.add_widget(self.runner)

        main_layout = BoxLayout(orientation= "vertical")
        main_layout.add_widget(layout1)
        main_layout.add_widget(self.sits)
        main_layout.add_widget(self.button)

        self.add_widget(main_layout)

    def next(self):
        self.manager.current = "pulse2"


class Pulse2Screen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        instr = Label(text= txt_test3)

        result2_label = Label(text= "Результат")
        self.result_2 = TextInput()
        result3_label = Label(text= "Результат після відпочинку")
        self.result_3 = TextInput()

        self.button = Button(text= "Почати")
        self.button.on_press = self.next

        layout1 = BoxLayout()
        layout1.add_widget(result2_label)
        layout1.add_widget(self.result_2)

        layout2 = BoxLayout()
        layout2.add_widget(result3_label)
        layout2.add_widget(self.result_3)

        main_layout = BoxLayout(orientation= "vertical")
        main_layout.add_widget(instr)
        main_layout.add_widget(layout1)
        main_layout.add_widget(layout2)
        main_layout.add_widget(self.button)

        self.add_widget(main_layout)
    
    def next(self):
        self.manager.current = "result"


class ResultScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.label = Label(text= "sdghdg")

        self.add_widget(self.label)

class HeartManager(App):
    def build(self):
        sm = ScreenManager()
        sm.add_widget(UserScreen(name="user"))
        sm.add_widget(Pulse1Screen(name="pulse1"))
        sm.add_widget(SitsScreen(name="sits"))
        sm.add_widget(Pulse2Screen(name="pulse2"))
        sm.add_widget(ResultScreen(name="result"))

        return sm

heart = HeartManager()
heart.run()