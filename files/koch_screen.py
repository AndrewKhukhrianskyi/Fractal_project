from tkinter import *
from tkinter import messagebox as mb

from files.eng.koch_func import KochClass
from files.eng.rnd import random_koch_func
from files.eng.converter import number_converter

from files.config.ui_config import *

class KochScreen:
    def __init__(self):
        self.width = KOCH_WIDTH
        self.height = KOCH_HEIGHT

    def koch_window(self):
        sub_root = Toplevel(width = self.width,
                            height = self.height,
                            bg = COLOR)
        sub_root.title(KOCH_TITLE)
        sub_root.resizable(False, False)
        
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
        
        def get_parameters():
            text_list = [length_field, l_angle_field, r_angle_field,
                        draw_angle_field, counter_field]
            arr = []

            for wdg in range(len(text_list)):
                if len(text_list[wdg].get(0.0, END)) > 4:
                    mb.showerror('Ошибка', "Какой-то из параметров принял большое значение! Я не буду рисовать!")
                    return 0
                
                if int(text_list[-1].get(0.0, END)) > 30:
                    mb.showerror('Ошибка', "Большой параметр цикла отрисовки. Измените его!")
                    return 0
                
                arr.append(text_list[wdg].get(0.0, END))
            
            draw_init = KochClass(number_converter(arr))
            draw_init.draw()

        def clear_parameters(*text_list):
            for wdg in text_list:
                wdg.delete(0.0, END)

        length_label = Label(sub_root,
                             width = LABEL_WIDTH,
                             height = LABEL_HEIGHT,
                             text = 'Длина линии',
                             bg = COLOR,
                             fg = TEXT)
        length_field = Text(sub_root, 
                            width = FIELD_WIDTH,
                            height = FIELD_HEIGHT,
                            bg = COLOR,
                            fg = TEXT)

        l_angle_label = Label(sub_root,
                             width = LABEL_WIDTH,
                             height = LABEL_HEIGHT,
                             text = 'Левый угол',
                             bg = COLOR,
                             fg = TEXT)

        l_angle_field = Text(sub_root,
                            width = FIELD_WIDTH,
                            height = FIELD_HEIGHT,
                            bg = COLOR,
                            fg = TEXT)

        r_angle_label = Label(sub_root,
                            width = LABEL_WIDTH,
                             height = LABEL_HEIGHT,
                             text = 'Правый угол',
                             bg = COLOR,
                             fg = TEXT)
        r_angle_field = Text(sub_root,
                            width = FIELD_WIDTH,
                            height = FIELD_HEIGHT,
                            bg = COLOR,
                            fg = TEXT)

        draw_angle_label = Label(sub_root,
                             width = LABEL_WIDTH,
                             height = LABEL_HEIGHT,
                             text = 'Угол отрисовки',
                             bg = COLOR,
                             fg = TEXT)
        draw_angle_field = Text(sub_root,
                            width = FIELD_WIDTH,
                            height = FIELD_HEIGHT,
                            bg = COLOR,
                            fg = TEXT)

        counter_label = Label(sub_root,
                             width = LABEL_WIDTH,
                             height = LABEL_HEIGHT,
                             text = 'Кол-во циклов отрисовки',
                             bg = COLOR,
                             fg = TEXT)
        counter_field = Text(sub_root,
                            width = FIELD_WIDTH,
                            height = FIELD_HEIGHT,
                            bg = COLOR,
                            fg = TEXT)
        
        draw_button = Button(sub_root,
                             width = KOCH_BUTTON_WIDTH,
                             height = KOCH_BUTTON_HEIGHT,
                             bg = COLOR,
                             fg = TEXT,
                             text = "Нарисовать",
                             command = get_parameters)

        empty_label = Label(sub_root,
                            width = LABEL_WIDTH,
                            height = LABEL_HEIGHT,
                            bg = COLOR)
        
        random_button = Button(sub_root,
                             width = KOCH_BUTTON_WIDTH,
                             height = KOCH_BUTTON_HEIGHT,
                             bg = COLOR,
                             fg = TEXT,
                             text = "Рандом",
                             command = rnd_messagebox)

        clear_data_button = Button(sub_root,
                             width = KOCH_BUTTON_WIDTH,
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
        clear_data_button.pack()
        draw_button.pack()

        
