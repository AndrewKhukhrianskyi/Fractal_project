from tkinter import *

from ui_config import *

class MainScreen:
    def __init__(self, width, height):
        self.width = width
        self.height = height
    
    def main_window(self):
        root = Tk()
        root.title(TITLE)
        root.geometry(f"{self.width}x{self.height}")
        root.resizable(False,False)
        root.config(bg = SCREEN_COLOR)

        koch_button = Button(text = KOCH_TEXT,
                             width = BUTTON_WIDTH,
                             height = BUTTON_HEIGHT,
                             bg = BUTTON_COLOR,
                             fg = TEXT_COLOR)
        
        l_curve_button = Button(text = L_TEXT,
                                width = BUTTON_WIDTH,
                                height = BUTTON_HEIGHT,
                                bg = BUTTON_COLOR,
                                fg = TEXT_COLOR)
        
        empty_label = Label(width = LABEL_WIDTH,
                            bg = LABEL_COLOR)
        
        koch_button.pack(side = TOP)
        empty_label.pack(side = TOP)
        l_curve_button.pack(side = TOP)
        
        root.mainloop()
        
if __name__ == '__main__':
    scr = MainScreen(WIDTH, HEIGHT)
    scr.main_window()
