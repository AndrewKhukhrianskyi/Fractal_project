import turtle
import re

from random import randint, choice

def randomize_rule():
    rnd_path = ''
    rnd_list = ['F', 'S', '+', '-', '[', ']']
    for rule in range(randint(5,20)):
        rnd_path += choice(rnd_list)

    return rnd_path


def cmd_turtle_fd(t, length, *args):
    t.pensize(args[1])
    t.fd(length*args[0])

def cmd_turtle_left(t, angle, *args):
    t.left(angle * args[0])

def cmd_turtle_right(t, angle, *args):
    t.right(angle * args[0])

class LSystem2D:
    def __init__(self, t, axiom, width, length, angle):
        self.axiom = axiom      
        self.state = axiom      
        self.width = width      
        self.length = length    
        self.angle = angle      
        self.t = t              
        self.rules = {}  
        self.t.pensize(self.width)
        self.function_key = None
        self.key_re_list = []  
        self.cmd_functions = {}  

    def add_rules(self, *rules):
        for key, value in rules:
            key_re = ""                     
            if not isinstance(value, str):  
                key_re = key.replace("(", r"\(")
                key_re = key_re.replace(")", r"\)")
                key_re = key_re.replace("+", r"\+")
                key_re = key_re.replace("-", r"\-")
                key_re = re.sub(r"([a-z]+)([, ]*)", lambda m: r"([-+]?\b\d+(?:\.\d+)?\b)" + m.group(2), key_re)
                self.key_re_list.append(key_re)

            self.rules[key] = (value, key_re)

    def update_param_cmd(self, m):
        if not self.function_key:
            return ""

        args = list(map(float, m.groups()))
        return self.function_key(*args).lower()

    def generate_path(self, n_iter):
        for n in range(n_iter):
            for key, values in self.rules.items():
                if isinstance(values[0], str):
                    self.state = self.state.replace(key, values[0].lower())
                else:   
                    self.function_key = values[0]
                    self.state = re.sub(values[1], self.update_param_cmd, self.state)
                    self.function_key = None

            self.state = self.state.upper()


    def set_turtle(self, my_tuple):
        self.t.up()
        self.t.goto(my_tuple[0], my_tuple[1])
        self.t.seth(my_tuple[2])
        self.t.down()

    def add_rules_move(self, *moves):
        for key, func in moves:
            self.cmd_functions[key] = func

    def draw_turtle(self, start_pos, start_angle):
            turtle.tracer(1, 0)
            self.t.up()  
            self.t.setpos(start_pos)  
            self.t.seth(start_angle)  
            self.t.down()  
            turtle_stack = []
            key_list_re = "|".join(self.key_re_list)
            # for move in self.state:
            for values in re.finditer(r"(" + key_list_re + r"|.)", self.state):
                cmd = values.group(0)
                args = [float(x) for x in values.groups()[1:] if x]

                if 'F' in cmd:
                    if len(args) > 0 and self.cmd_functions.get('F'):
                        self.cmd_functions['F'](t, self.length, *args)
                    else:
                        self.t.fd(self.length)
                elif 'S' in cmd:
                    if len(args) > 0 and self.cmd_functions.get('S'):
                        self.cmd_functions['S'](t, self.length, *args)
                    else:
                        self.t.up()
                        self.t.forward(self.length)
                        self.t.down()
                elif '+' in cmd:
                    if len(args) > 0 and self.cmd_functions.get('+'):
                        self.cmd_functions['+'](t, self.angle, *args)
                    else:
                        self.t.left(self.angle)
                elif '-' in cmd:
                    if len(args) > 0 and self.cmd_functions.get('-'):
                        self.cmd_functions['-'](t, self.angle, *args)
                    else:
                        self.t.right(self.angle)
                elif "[" in cmd:
                    turtle_stack.append((self.t.xcor(), self.t.ycor(), self.t.heading(), self.t.pensize()))
                elif "]" in cmd:
                    xcor, ycor, head, w = turtle_stack.pop()
                    self.set_turtle((xcor, ycor, head))
                    self.width = w
                    self.t.pensize(self.width)

            turtle.done()        



width = 1200
height = 600
screen = turtle.Screen()
screen.setup(width, height, 0, 0)


t = turtle.Turtle()
t.ht()          

pen_width = 2   
f_len = 20     
angle = 33

axiom = "A"

l_sys = LSystem2D(t, axiom, pen_width, f_len, angle)

l_sys.add_rules(("A", "F(1, 1)[+(1)A][-(1)A]"),
                ("F(x, y)", lambda x, y: f"F({1.5*x}, {1.7*y})"),
                ("+(x)", lambda x: f"+({1.1*x})"),
                ("-(x)", lambda x: f"-({1.1*x})"),
                )

l_sys.add_rules_move(("F", cmd_turtle_fd), ("+", cmd_turtle_left), ("-", cmd_turtle_right))
l_sys.generate_path(5)
print(l_sys.state)
l_sys.draw_turtle( (0, -200), 90)
