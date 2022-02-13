''' Kivy version 
# Import custom modules
from ui_config import *
from eng.koch_func import *
# Kivy UI
from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout
from kivy.config import Config


#stats = ['0', '450', '450']
#opts = ['resizable', 'width', 'height']
    

Config.set('graphics', 'resizable', '0')
Config.set('graphics', 'width', '700')
Config.set('graphics', 'height', '200')

class FractalProjectApp(App):
    def build(self):
        layout = GridLayout(cols=2)
        for elem in range(len(TEXT)):
            layout.add_widget(Button(text = TEXT[elem],
                              background_color =  BG_COLOR,
                              font_size = FONT_SIZE,
                              border = BORDERS,
                              on_press = self.btn_press))
        return layout
    def btn_press(self, instance):
        KochClass(6, 30, 180).draw()
        

if __name__ == '__main__':
    FractalProjectApp().run()
'''
