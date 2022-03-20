from tkinter import *
from tkinter import messagebox as mb

<<<<<<< HEAD
from
=======
from files.config.ui_config import *
from files.eng.rnd import random_l_func

class LCurveScreen:
    def __init__(self):
        self.width = L_CURVE_WIDTH
        self.height = L_CURVE_HEIGHT
    
    def l_window(self):
        l_root = Toplevel(width = self.width,
                        height = self.height,
                        bg = COLOR)
        l_root.title(L_TITLE)
        l_root.resizable(False, False)
        l_root.geometry(f'{self.width}x{self.height}')

        def rnd_messagebox():
            ans = mb.askyesno(title = "Вопрос",
                              message = "Вы уверены, что хотите случайно выбрать данные?")
            if ans == True:
                add_rnd_parameters(axiom_field, width_field,
                                  length_field, angle_field)
                mb.showinfo("Окошко", "Данные сгенерированы.")

        def clear_messagebox():
            ans = mb.askyesno(title = "Вопрос",
                              message = "Вы уверены, что хотите очистить все данные?")
            if ans == True:
                clear_parameters(axiom_field, width_field,
                                length_field, angle_field)
                mb.showinfo("Окошко", "Данные стерты.")
        
        def add_rnd_parameters(*text_list):
            data = random_l_func()
            for wdg in range(len(text_list)):
                text_list[wdg].insert(0.0, data[wdg]) 
        
        def clear_parameters(*text_list):
            for wdg in text_list:
                wdg.delete(0.0, END)

        axiom_label = Label(l_root,
                            width = LABEL_WIDTH,
                            height = LABEL_HEIGHT,
                            text = 'Правило',
                            bg = COLOR,
                            fg = TEXT)
        axiom_field = Text(l_root,
                           width = LABEL_WIDTH,
                            height = LABEL_HEIGHT + 3,
                            bg = COLOR,
                            fg = TEXT)

        width_label = Label(l_root,
                            width = LABEL_WIDTH,
                            height = LABEL_HEIGHT,
                            text = 'Толщина кисти',
                            bg = COLOR,
                            fg = TEXT)
        width_field = Text(l_root,
                           width = LABEL_WIDTH,
                            height = LABEL_HEIGHT,
                            bg = COLOR,
                            fg = TEXT)

        length_label = Label(l_root,
                            width = LABEL_WIDTH,
                            height = LABEL_HEIGHT,
                            text = 'Длина кривой',
                            bg = COLOR,
                            fg = TEXT)
        length_field = Text(l_root,
                           width = LABEL_WIDTH,
                            height = LABEL_HEIGHT,
                            bg = COLOR,
                            fg = TEXT)

        angle_label = Label(l_root,
                            width = LABEL_WIDTH,
                            height = LABEL_HEIGHT,
                            text = 'Угол отрисовки',
                            bg = COLOR,
                            fg = TEXT)
        angle_field = Text(l_root,
                           width = LABEL_WIDTH,
                            height = LABEL_HEIGHT,
                            bg = COLOR,
                            fg = TEXT)
        
        empty_label = Label(l_root,
                            width = LABEL_WIDTH,
                            height = LABEL_HEIGHT,
                            bg = COLOR)
        rand_btn = Button(l_root,
                          width = BUTTON_WIDTH,
                          height = BUTTON_HEIGHT,
                          bg = COLOR,
                          fg = TEXT,
                          command = rnd_messagebox,
                          text = 'Рандом')
        clr_btn = Button(l_root,
                          width = BUTTON_WIDTH,
                          height = BUTTON_HEIGHT,
                          bg = COLOR,
                          fg = TEXT,
                          command = clear_messagebox,
                          text = 'Очистить')
        draw_btn = Button(l_root,
                          width = BUTTON_WIDTH,
                          height = BUTTON_HEIGHT,
                          bg = COLOR,
                          fg = TEXT,
                          text = 'Старт!')

        wdg_arr = [axiom_label, axiom_field,
                   width_label, width_field,
                   length_label, length_field,
                   angle_label, angle_field, empty_label,
                   rand_btn, clr_btn, draw_btn]
        
        for wdg in wdg_arr:
            wdg.pack()

>>>>>>> 7038cb966e40850f8fb83bd7f1c7ef3bf9c88f90
