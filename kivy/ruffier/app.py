from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.screenmanager import Screen, ScreenManager
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput


name = str()
age = 7
p1, p2, p3 = 0, 0, 0


class InstrScr(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        instruction = Label(text='Инструкция')
        name_lbl = Label(text='Введите ваше имя:')
        age_lbl = Label(text='Введите ваш возраст:')
        self.btn = Button(text='Начать')
        self.btn.on_press = self.next
        self.name_input = TextInput(multiline=False)
        self.age_input = TextInput(multiline=False)
        name_layout = BoxLayout()
        age_layout = BoxLayout()
        main_layout = BoxLayout(orientation='vertical')
        name_layout.add_widget(name_lbl)
        name_layout.add_widget(self.name_input)
        age_layout.add_widget(age_lbl)
        age_layout.add_widget(self.age_input)
        main_layout.add_widget(instruction)
        main_layout.add_widget(name_layout)
        main_layout.add_widget(age_layout)
        main_layout.add_widget(self.btn)
        self.add_widget(main_layout)

    def next(self):
        global name, age
        name = self.name_input.text
        age = int(self.age_input.text)
        print(name, age)
        #self.manager.current = 'pulse1'


class MyApp(App):
    def build(self):
        sm = ScreenManager()
        sm.add_widget(InstrScr(name='main'))
        return sm


app = MyApp()
app.run()
