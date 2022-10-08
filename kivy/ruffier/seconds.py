from kivy.uix.label import Label
from kivy.clock import Clock
from kivy.properties import BooleanProperty


class Seconds(Label):
    done = BooleanProperty(False)
    
    def __init__(self, total, **kwargs):
        self.current = total
        my_text = 'Осталось: ' + str(self.current)
        super().__init__(text=my_text)

    def start(self):
        Clock.schedule_interval(self.change, 1)

    def restart(self, total):
        self.current = total
        self.done = False
        self.text = 'Осталось: ' + str(self.current)
        self.start()

    def change(self, dt):
        self.current -= 1
        self.text = 'Осталось: ' + str(self.current)
        if self.current <= 0:
            self.done = True
            return False
