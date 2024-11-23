from kivy.uix.label import Label


class Sits(Label):
    
    def __init__(self, total, **kwargs):
        self.total = total
        self.current = 0
        my_text = "Залишилось присідань: " + str(self.total)
        super().__init__(text= my_text, **kwargs)

    def next(self, *args):
        self.current += 1
        diference = self.total - self.current
        my_text = "Залишилось присідань: " + str(diference)
        self.text = my_text