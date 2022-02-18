from tkinter import *
from tkinter import messagebox as mb

from eng.koch_func import KochClass
from eng.rnd import random_koch_func
from eng.converter import number_converter

from config.ui_config import *

class KochScreen:
    def __init__(self):
        self.width = KOCH_WIDTH
        self.height = KOCH_HEIGHT
    

    def koch_window(self):
        sub_root = Toplevel()
        sub_root.title(KOCH_TITLE)
        sub_root.geometry(f"{self.width}x{self.height}")
        sub_root.resizable(False, False)
        sub_root.config(bg = COLOR)
        
        def rnd_messagebox():
            ans = mb.askyesno(title = "Вопрос",
                              message = "Вы уверены, что хотите случайно выбрать данные?")
            if ans == True:
                add_rnd_parameters(length_field, l_angle_field,
                               r_angle_field, draw_angle_field,
                               counter_field)
                mb.showinfo("Окошко", "Данные сгенерированы.")

        def clear_messagebox():
            ans = mb.askyesno(title = "Вопрос",
                              message = "Вы уверены, что хотите очистить все данные?")
            if ans == True:
                clear_parameters(length_field, l_angle_field,
                               r_angle_field, draw_angle_field,
                               counter_field)
                mb.showinfo("Окошко", "Данные стерты.")
        
        def add_rnd_parameters(*text_list):
            data = random_koch_func()
            for wdg in range(len(text_list)):
                text_list[wdg].insert(0.0, data[wdg])
        
        def get_parameters(*text_list):
            arr = []
            for wdg in range(len(text_list)):
                arr.append(text_list[wdg].get(0.0, END))
            
            number_converter(arr)

        def clear_parameters(*text_list):
            for wdg in text_list:
                wdg.delete(0.0, END)

        length_label = Label(width = LABEL_WIDTH,
                             height = LABEL_HEIGHT,
                             text = 'Длина линии',
                             bg = COLOR,
                             fg = TEXT)
        length_field = Text(width = FIELD_WIDTH,
                            height = FIELD_HEIGHT,
                            bg = COLOR,
                            fg = TEXT)

        l_angle_label = Label(width = LABEL_WIDTH,
                             height = LABEL_HEIGHT,
                             text = 'Левый угол',
                             bg = COLOR,
                             fg = TEXT)

        l_angle_field = Text(width = FIELD_WIDTH,
                            height = FIELD_HEIGHT,
                            bg = COLOR,
                            fg = TEXT)

        r_angle_label = Label(width = LABEL_WIDTH,
                             height = LABEL_HEIGHT,
                             text = 'Правый угол',
                             bg = COLOR,
                             fg = TEXT)
        r_angle_field = Text(width = FIELD_WIDTH,
                            height = FIELD_HEIGHT,
                            bg = COLOR,
                            fg = TEXT)

        draw_angle_label = Label(width = LABEL_WIDTH,
                             height = LABEL_HEIGHT,
                             text = 'Угол отрисовки',
                             bg = COLOR,
                             fg = TEXT)
        draw_angle_field = Text(width = FIELD_WIDTH,
                            height = FIELD_HEIGHT,
                            bg = COLOR,
                            fg = TEXT)

        counter_label = Label(width = LABEL_WIDTH,
                             height = LABEL_HEIGHT,
                             text = 'Кол-во циклов отрисовки',
                             bg = COLOR,
                             fg = TEXT)
        counter_field = Text(width = FIELD_WIDTH,
                            height = FIELD_HEIGHT,
                            bg = COLOR,
                            fg = TEXT)
        
        draw_button = Button(width = KOCH_BUTTON_WIDTH,
                             height = KOCH_BUTTON_HEIGHT,
                             bg = COLOR,
                             fg = TEXT,
                             text = "Нарисовать",
                             command = KochClass(get_parameters(
                                length_field, l_angle_field,
                                r_angle_field, draw_angle_field,
                                counter_field))).draw()

        empty_label = Label(width = LABEL_WIDTH,
                            height = LABEL_HEIGHT,
                            bg = COLOR)
        
        random_button = Button(width = KOCH_BUTTON_WIDTH,
                             height = KOCH_BUTTON_HEIGHT,
                             bg = COLOR,
                             fg = TEXT,
                             text = "Рандом",
                             command = rnd_messagebox)

        clear_button = Button(width = KOCH_BUTTON_WIDTH,
                             height = KOCH_BUTTON_HEIGHT,
                             bg = COLOR,
                             fg = TEXT,
                             text = "Очистить",
                             command = clear_messagebox)

        

        length_label.pack()
        length_field.pack()
        
        l_angle_label.pack()
        l_angle_field.pack()
        
        r_angle_label.pack()
        r_angle_field.pack()

        draw_angle_label.pack()
        draw_angle_field.pack()

        counter_label.pack()
        counter_field.pack()

        empty_label.pack()
        random_button.pack()
        clear_button.pack()
        draw_button.pack()