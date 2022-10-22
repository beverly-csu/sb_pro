from kivy.animation import Animation
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout


class Runner(BoxLayout):
    def __init__(self, total=10, steptime=1.0, **kwargs):
        super().__init__(**kwargs)
        self.total = total
        self.steptime = steptime
        anim1 = Animation(pos_hint={'top': 0.1}, duration=steptime/2)
        anim2 = Animation(pos_hint={'top': 1.0}, duration=steptime/2)
        self.anim = anim1 + anim2
        self.btn = Button(size_hint=(1.0, 0.1), pos_hint={'top': 1.0}, background_color=(1, 1, 1, 1))
        self.anim.repeat = True
        self.anim.on_progress = self.next
        self.add_widget(self.btn)

    def start(self):
        self.level = 0
        self.anim.start(self.btn)

    def next(self, widget, step):
        if step == 1.0:
            self.level += 1
            if self.level >= self.total:
                self.anim.repeat = False
