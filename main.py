from tkinter import *

from files.config.ui_config import *
from files.eng.koch_func import KochClass
from files.koch_screen import KochScreen


class MainScreen:
    def __init__(self):
        self.width = WIDTH
        self.height = HEIGHT
    
    def main_window(self):
        root = Tk()
        root.title(TITLE)
        root.geometry(f"{self.width}x{self.height}")
        root.resizable(False,False)
        root.config(bg = COLOR)

        koch_button = Button(text = KOCH_TEXT,
                             width = BUTTON_WIDTH,
                             height = BUTTON_HEIGHT,
                             bg = COLOR,
                             fg = TEXT,
                             command = KochScreen().koch_window)               
        
        l_curve_button = Button(text = L_TEXT,
                                width = BUTTON_WIDTH,
                                height = BUTTON_HEIGHT,
                                bg = COLOR,
                                fg = TEXT)
        
        empty_label = Label(width = LABEL_WIDTH,
                            bg = COLOR)
        
        koch_button.pack(side = TOP)
        empty_label.pack(side = TOP)
        l_curve_button.pack(side = TOP)
        
        root.mainloop()
        
if __name__ == '__main__':
    MainScreen().main_window()
