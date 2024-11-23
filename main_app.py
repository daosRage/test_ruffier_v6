from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.core.window import Window

from instructions import *
from seconds import Seconds
from sits import Sits
from runner import Runner
from ruffier import *

Window.clearcolor = (1, 0, 0, 1)


def check_int(value):
    try:
        return int(value)
    except: 
        return False


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
        global name, age
        name = self.name_pac.text
        age = check_int(self.age.text)
        if age == False or age < 7:
            age = 7
            self.age.text = str(age)
        else:
            self.manager.current = "pulse1"


class Pulse1Screen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.next_screen = False

        instr = Label(text= txt_test1)
        self.timer = Seconds(3)
        self.timer.bind(done= self.timer_finish)

        result_label = Label(text= "Введіть результати")
        self.result = TextInput()
        self.result.set_disabled(True)

        self.button = Button(text= "Почати")
        self.button.on_press = self.next

        layout1 = BoxLayout()
        layout1.add_widget(result_label)
        layout1.add_widget(self.result)

        main_layout = BoxLayout(orientation= "vertical")
        main_layout.add_widget(instr)
        main_layout.add_widget(self.timer)
        main_layout.add_widget(layout1)
        main_layout.add_widget(self.button)

        self.add_widget(main_layout)

    def timer_finish(self, *args):
        self.result.set_disabled(False)
        self.button.set_disabled(False)
        self.next_screen = True
        self.button.text = "Продовжити"
    
    def next(self):
        if not self.next_screen:
            self.button.set_disabled(True)
            self.timer.start()
        else:
            global result1
            result1 = check_int(self.result.text)

            if result1 == False or result1 <= 0:
                result1 = 0
                self.result.text = str(result1)
            else:
                self.manager.current = "sits"


class SitsScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.next_screen = False

        instr = Label(text= txt_test2)
        self.sits = Sits(4)
        self.runner = Runner(total= 4, size_hint= (0.4, 1))
        self.runner.bind(finished= self.run_finished)

        self.button = Button(text= "Почати")
        self.button.on_press = self.next

        vl = BoxLayout(orientation= "vertical")
        vl.add_widget(instr)
        vl.add_widget(self.sits)

        layout1 = BoxLayout()
        layout1.add_widget(vl)
        layout1.add_widget(self.runner)

        main_layout = BoxLayout(orientation= "vertical")
        main_layout.add_widget(layout1)
        main_layout.add_widget(self.button)

        self.add_widget(main_layout)

    def run_finished(self, *args):
        self.button.set_disabled(False)
        self.button.text = "Продовжити"
        self.next_screen = True

    def next(self):
        if self.next_screen:
            self.manager.current = "pulse2"
        else:
            self.runner.start()
            self.runner.bind(value= self.sits.next)
            self.button.set_disabled(True)

class Pulse2Screen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.next_screen = False
        self.stage = 0

        self.timer = Seconds(3)
        self.timer.bind(done= self.timer_finish)

        instr = Label(text= txt_test3)
        self.instr2 = Label()

        result2_label = Label(text= "Результат")
        self.result_2 = TextInput()
        result3_label = Label(text= "Результат після відпочинку")
        self.result_3 = TextInput()
        self.result_2.set_disabled(True)
        self.result_3.set_disabled(True)

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
        main_layout.add_widget(self.instr2)
        main_layout.add_widget(self.timer)
        main_layout.add_widget(layout1)
        main_layout.add_widget(layout2)
        main_layout.add_widget(self.button)

        self.add_widget(main_layout)
    
    def timer_finish(self, *args):
        if self.timer.done == True:
            if self.stage == 0:
                self.stage = 1
                self.timer.restart(5)
                self.result_2.set_disabled(False)
                self.instr2.text = "Відпочивайте"
            elif self.stage == 1:
                self.stage = 2
                self.timer.restart(3)
                self.instr2.text = "Міряйте пульс"
            elif self.stage == 2:
                self.button.set_disabled(False)
                self.result_3.set_disabled(False)
                self.next_screen = True
                self.instr2.text = ""

    
    def next(self):
        if not self.next_screen:
            self.button.set_disabled(True)
            self.timer.start()
            self.instr2.text = "Міряйте пульс"
        else:
            global result2, result3
            result2 = check_int(self.result_2.text)
            result3 = check_int(self.result_3.text)

            if result2 == False or result2 <= 0:
                result2 = 0
                self.result_2.text = str(result2)
            if result3 == False or result3 <= 0:
                result3 = 0
                self.result_3.text = str(result3)
            else:
                self.manager.current = "result"


class ResultScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.label = Label(text= "sdghdg")

        self.add_widget(self.label)

        self.on_enter = self.before

    def before(self):
        self.label.text = f"Ваше ім'я: {name}\n{txt_index}{ruffier_index(result1, result2, result3)}\n{txt_workheart}{test(result1,result2,result3, age)}"

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