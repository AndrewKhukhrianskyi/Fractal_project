from tkinter import *

from files.config.ui_config import *
from files.koch_screen import KochScreen
from files.l_curve_screen import LCurveScreen


class MainScreen:
    def main_window(self):
        root = Tk()
        root.title(TITLE)
        root.geometry(f"{WIDTH}x{HEIGHT}")
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
                                fg = TEXT,
                                command = LCurveScreen().l_window)
        
        empty_label = Label(width = LABEL_WIDTH,
                            bg = COLOR)
        widgets = [koch_button,
                   empty_label,
                   l_curve_button]
        for widget in widgets:
            widget.pack(side = TOP)
        
        root.mainloop()
        
if __name__ == '__main__':
    MainScreen().main_window()