from kivy.uix.screenmanager import Screen
from kivy.uix.button import Button
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.image import Image
from kivy.uix.behaviors.button import ButtonBehavior
from kivy.vector import Vector
from kivy.app import App

class MenuScreen(Screen):
    def __init__(self, **kwargs):
        super(MenuScreen, self).__init__(**kwargs)
        self.audiometer = kwargs['audiometer']
        self.screen_manager = self.audiometer.root

        layout = FloatLayout()
        go_to_demo_button = Button(text="Home", font_size=40, size_hint=(.25, .5),background_normal = "images/button.png", color = (0,0,0,1), background_color = (0.9,0.9,0,1),pos = (60,180))

        go_to_hearing_button = Button(text="       Take \nHearing Test", background_color = (0.9,0.9,0,1),background_normal = "images/button.png",font_size=30, color = (0,0,0,1), size_hint=(.25, .5),pos = (300, 180))
        #go_to_results_button = Button(text="results", font_size=40)
        go_to_testresults_button = Button(text="Test Results", background_normal = "images/button.png", font_size=30, color = (0,0,0,1), size_hint=(.25, .5), background_color = (0.9,0.9,0,1),pos = (540,180))

        exit = Button(text="Exit", background_color = (1,0,0,0.8), font_size = 20, size_hint=(.15, .15),pos = (20,20))
        exit.bind(on_release=self.exit)
        

        go_to_demo_button.bind(on_release=self.go_to_demo)
        go_to_hearing_button.bind(on_release=self.go_to_hearing)
        #go_to_results_button.bind(on_press=self.go_to_results)
        go_to_testresults_button.bind(on_release=self.go_to_testresults)

        layout.add_widget(go_to_demo_button)
        layout.add_widget(go_to_hearing_button)
        #layout.add_widget(go_to_results_button)
        layout.add_widget(go_to_testresults_button)
        layout.add_widget(exit)
        
        self.add_widget(layout)

    def go_to_demo(self, instance):
        self.screen_manager.current = 'home'
        self.screen_manager.transition.direction='right'

    def go_to_hearing(self, instance):
        self.audiometer.test.test_freqs = [250, 500, 1000, 2000, 4000, 8000]
        self.screen_manager.current = 'hearing'
        self.screen_manager.transition.direction='left'

    #def go_to_results(self, instance):
     #   self.screen_manager.current = 'results'

    def go_to_testresults(self, instance):
        self.screen_manager.current = 'testresults'
        self.screen_manager.transition.direction='left'    

    def exit(self, instance):
        App.get_running_app().stop()