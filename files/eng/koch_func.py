# Добавление библиотек для отрисовки
import turtle

from files.config.eng_config import *
# Класс работы со снежинкой Коха
class KochClass:
    # Передаем параметры длины и углов для отрисовки
    def __init__(self, datas):
        self.length = datas[0] # длина
        self.l_angle = datas[1] # левый угол
        self.r_angle = datas[2] # правый угол
        self.draw_angle = datas[3] # угол отрисовки
        self.counter = datas[4] # кол-во линий
       
    def draw_koch_segment(self, t, line):
        """ Условие залома линии. Если длина больше 6,
            то мы заламываем линию разделив ее на 3 и выполняем рекурсию
            иначе - отрисовываем линию"""
        t.hideturtle()
        if line > 6:
            short_line = line // 3
            self.draw_koch_segment(t, short_line)
            t.left(self.l_angle)
            self.draw_koch_segment(t, short_line)
            t.right(self.r_angle)
            self.draw_koch_segment(t, short_line)
            t.left(self.l_angle)
            self.draw_koch_segment(t, short_line)
        else:
            t.fd(line)
            t.left(self.l_angle)
            t.fd(line)
            t.right(self.r_angle)
            t.fd(line)
            t.left(self.l_angle)
            t.fd(line)

    # Работа с Turtle. Создание окон, назначение переменных и тд.
    def draw(self):
        try:
            t = turtle.Turtle()
            turtle.TurtleScreen._RUNNING = True
            t.ht()
            t.speed(TURTLE_SPEED)
        
            screen = turtle.Screen()
            screen.setup(TURTLE_WIDTH, TURTLE_HEIGHT, TURTLE_RESIZE_X, TURTLE_RESIZE_Y)
            
            for elem in range(self.counter):
                t.left(self.draw_angle)
                self.draw_koch_segment(t, self.length)
    
            turtle.done()
        except turtle.Terminator: # Тут надо логику менять для Turtle исключений
            self.draw()    

# TODO
'''
1. Сохранять объект окна в классе для повторного его открытия ИЛИ создавать новый объект окна в классе при попытке открытия.
2. Вероятно, надо будет обработать исключения для работы
3. Вполне вероятно - расписать отдельный класс для работы с Turtle и дописать ему методы, которые будут в п.1 
'''