from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.screenmanager import Screen, ScreenManager
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput
from kivy.uix.popup import Popup
from instructions import *                                                                                                      ####
from seconds import Seconds                                                                                                     ####


name = str()
age = 7
p1, p2, p3 = 0, 0, 0


class InstrScr(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        instruction = Label(text=txt_instruction)                                                                               ####
        name_lbl = Label(text='Введите ваше имя:')
        age_lbl = Label(text='Введите ваш возраст:')
        self.btn = Button(text='Начать', size_hint=(0.3, None), height='30sp', pos_hint={'center_x': 0.5, 'center_y': 0.5})     ####
        self.btn.on_press = self.next
        self.name_input = TextInput(multiline=False)
        self.age_input = TextInput(multiline=False)
        name_layout = BoxLayout(size_hint=(0.8, None), height='30sp', pos_hint={'center_x': 0.5, 'center_y': 0.5})              ####
        age_layout = BoxLayout(size_hint=(0.8, None), height='30sp', pos_hint={'center_x': 0.5, 'center_y': 0.5})               ####
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
        try:
            age = int(self.age_input.text)
            self.manager.current = 'pulse1'
        except:
            popup = Popup(content=Label(text="Введите возраст правильно!"))
            popup.open()


class PulseScr(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        instruction = Label(text='Здесь нужно будет ввести пульс')
        self.pulse_input = TextInput(multiline=False)
        pulse_lbl = Label(text='Введите пульс:')
        self.btn = Button(text='Продолжить')
        self.btn.on_press = self.next
        self.seconds = Seconds(15)                                                                                  ####

        pulse_layout = BoxLayout()
        main_layout = BoxLayout(orientation='vertical')

        pulse_layout.add_widget(pulse_lbl)
        pulse_layout.add_widget(self.pulse_input)
        main_layout.add_widget(instruction)
        main_layout.add_widget(self.seconds)                                                                        ####
        main_layout.add_widget(pulse_layout)
        main_layout.add_widget(self.btn)

        self.add_widget(main_layout)

    def next(self):
        self.seconds.start()                                                                                        ####
        #### self.manager.current = 'sits'


class CheckSits(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        instruction = Label(text='Вам надо присесть 30 раз')
        self.btn = Button(text='Продолжить')
        self.btn.on_press = self.next
        layout = BoxLayout(orientation='vertical')
        layout.add_widget(instruction)
        layout.add_widget(self.btn)
        self.add_widget(layout)

    def next(self):
        self.manager.current = 'pulse2'


class PulseScr2(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        instruction = Label(text='Инструкция')
        self.pulse_inp_1 = TextInput(multiline=False)
        self.pulse_inp_2 = TextInput(multiline=False)
        pulse_lbl_1 = Label(text='Первый замер:')
        pulse_lbl_2 = Label(text='Второй замер:')
        self.btn = Button(text='Продолжить')
        self.btn.on_press = self.next
        pulse1 = BoxLayout()
        pulse2 = BoxLayout()
        main_layout = BoxLayout(orientation='vertical')
        pulse1.add_widget(pulse_lbl_1)
        pulse1.add_widget(self.pulse_inp_1)
        pulse2.add_widget(pulse_lbl_2)
        pulse2.add_widget(self.pulse_inp_2)
        main_layout.add_widget(instruction)
        main_layout.add_widget(pulse1)
        main_layout.add_widget(pulse2)
        main_layout.add_widget(self.btn)

        self.add_widget(main_layout)

    def next(self):
        pass


class MyApp(App):
    def build(self):
        sm = ScreenManager()
        sm.add_widget(InstrScr(name='main'))
        sm.add_widget(PulseScr(name='pulse1'))
        sm.add_widget(CheckSits(name='sits'))
        sm.add_widget(PulseScr2(name='pulse2'))
        return sm


app = MyApp()
app.run()