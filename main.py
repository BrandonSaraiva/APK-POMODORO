from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.clock import Clock
from kivy.properties import ObjectProperty
from kivy.uix.widget import Widget
from kivy.core.audio import SoundLoader
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.config import Config
import os, sys
from kivy.resources import resource_add_path, resource_find

# Configurações do display da tela
Config.set('graphics', 'width', '400')
Config.set('graphics', 'height', '600')
Config.set('graphics', 'resizable', '0')
Config.write()
###################################

class Timer(Widget):
    work_time, padrao = 3000, 3000
    break_time = 600
    long_break = 1800
    sequencia = ['Work', 'Break', 'Work', 'Break', 'Work', 'Break', 'Work', 'Long Break']
    ciclo = 0
    contador = 1
    completo = 0
    timer_On = False

    def __init__(self, **kwargs):
        super(Timer, self).__init__(**kwargs)
        Clock.schedule_interval(self.update, 1)

    #Convertendo em minutos e segundos
    def conversor_tempo(self):
        self.minutes, self.seconds = divmod(self.work_time, 60)
        return str("%d:%02d" %(self.minutes, self.seconds))

    #Startando
    def start_timer(self):
        self.timer_On = True

    #Stopando
    def stop_timer(self):
        self.timer_On = False

    # Resetando tudo
    def reset_timer(self):
        self.ciclo = 0
        self.contador = 1
        self.completo = 0
        self.timer_On = False
        self.work_time = self.padrao
        self.completeLabel.text = 'Zerou: ' + str(self.completo)

    # Checando se completou todos os 4 ciclos
    def check_cycle(self):
        if self.ciclo < 7:
            self.ciclo += 1
        else:
            self.ciclo = 0

        self.setup()

    # Setando o status pra work,break,long etc
    def setup(self):
        self.statusLabel.text = str('Status: ' + self.sequencia[self.ciclo])
        if self.sequencia[self.ciclo] == 'Work':
            #Mudando o som compativel com o status
            alarme = SoundLoader.load('Resources/vamos.mp3')
            alarme.play()
            ###############
            self.work_time = self.padrao
            self.contador += 1
            if self.contador == 4:
                self.contador = 0
        elif self.sequencia[self.ciclo] == 'Break':
            # Mudando o som compativel com o status
            alarme = SoundLoader.load('Resources/ah_e.mp3')
            alarme.play()
            ###############
            self.cycleLabel.text = 'Ciclos completados: ' + str(self.contador) + '/4'
            self.work_time = self.break_time

            self.completeLabel.text = 'Zerou: ' + str(self.completo)
        else:
            self.cycleLabel.text = 'Ciclos completados: ' + str(self.contador) + '/4'
            self.work_time = self.long_break

            self.completo += 1

            if self.completo == 2:
                self.completeLabel.text = 'Zerou: ' +  str(self.completo) + '!!! Boa garaio'
                return

            self.completeLabel.text = 'Zerou: ' +  str(self.completo)

        if self.timer_On is False:
            self.btn_default()
        else:
            self.pause_default()

    # Estilizando o botao de pause
    def pause_default(self):
        self.main_btn.background_normal = './Resources/pause.jpg'
        self.main_btn.background_down = './Resources/pause.jpg'


    # Estilizando o botao de start
    def btn_default(self):
        self.main_btn.background_normal = './Resources/play.jpg'
        self.main_btn.background_down = './Resources/play.jpg'

    # Start/Pause Button
    def start_button(self):
        if self.timer_On:
            self.btn_default()
            self.stop_timer()
        else:
            self.pause_default()
            self.start_timer()

    # Button pra skipar pra prox fase
    def break_button(self):
        self.timer_On = True
        self.check_cycle()

    # Resetando todos os contadores
    def reset_button(self):
        self.completo = 0
        self.reset.disabled = True
        self.reset_timer()
        self.displayLabel.text = str(self.conversor_tempo())
        self.cycleLabel.text = "Completed Cycles: 0/4"
        self.statusLabel.text = "Status: Work"
        self.btn_default()

    #Controla oq aparece na tela, os minutos diminuindo ou msg de acabar por exemplo
    def update(self, *args, **kwargs):
        if self.timer_On and self.work_time > 0:
            self.reset.disabled = False
            self.work_time -= 1
            self.displayLabel.text = self.conversor_tempo()
            self.displayLabel.font_size = "100"
        elif self.work_time == 0:
            self.timer_On = False
            self.displayLabel.text = "CABOUCI!"
            self.displayLabel.font_size = "50"
            self.check_cycle()

class TimerScreen(Screen):
    pass

class Manager(ScreenManager):
    pass

class PomoApp(App):
    pass

if __name__ == '__main__':
    if hasattr(sys, '_MEIPASS'):
        resource_add_path(os.path.join(sys._MEIPASS))
    PomoApp().run()

