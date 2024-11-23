from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.animation import Animation
from kivy.properties import BooleanProperty, NumericProperty

class Runner(BoxLayout):
    value = NumericProperty(0)
    finished = BooleanProperty(False)

    def __init__(self, total, steptime= 1.5, **kwargs):
        super().__init__(**kwargs)
        self.total = total
        self.progress = "Присідання"
        self.animation = (Animation(pos_hint= {"top": 0.1}, duration= steptime / 2)
                          + Animation(pos_hint= {"top": 1}, duration= steptime / 2))
        self.animation.repeat = True
        self.animation.on_progress = self.next
        self.button = Button(size_hint= (1, 0.1), pos_hint= {"top": 1.0})
        self.add_widget(self.button)

    def start(self):
        self.value = 0
        self.finished = False
        self.button.text = self.progress
        self.animation.repeat = True
        self.animation.start(self.button)

    def next(self, widget, step):
        if step == 1.0:
            self.value += 1
            if self.value >= self.total:
                self.animation.repeat = False
                self.finished = True