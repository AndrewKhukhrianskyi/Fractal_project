# Fractal_project
Fractal Project is an application which helps users to create awesomes paintings by using fractal system :).

## Getting started
Before we start our guideline about project we should understand, which technologies are used for app creation.
All process was written on the Python Language and special python instruments (modules).

### Prerequisites
UI Modules
1. Tkinter
2. Kivy (In future :D)

Funcional modules
1. random
2. os
3. turtle

Programming languages
1. Python v.3.10.2
2. Kivy language (in future, again :D)

### Installing
1. Install Python programing language. Link: https://www.python.org/downloads/
2. By using terminal, go to the Fractal Project file and write the next command
```
python main.py
```

## Manual guideline
In current part we should understand how project works.
### Koch system
Koch system is a fractal system which is based on building fractal objects which is looks like as a snowflake :)
#### Example
![koch_fractal_example](https://user-images.githubusercontent.com/55056139/154777775-33156f51-a0fb-48c1-a19e-5856932453ee.png)
Snowflake drawing requires the next parameters:
1. Line length;
2. Left & Right angles (requires for the line curvature);
3. Draw angle;
4. Line counter (how many times we should draw the line?).

### Koch UI
![koch_menu](https://user-images.githubusercontent.com/55056139/154777951-828beb45-116d-4dcf-b063-4f053ab3d6e7.png)
#### Instruction
The current menu has five text fields and three buttons. All text fields are chronologically placed according to the list above.
1. "Рандом" button is used to randomize all parameters and add them to the text fields;
2. "Очистить" button is used to clear all data from all text fields;
3. "Нарисовать" button is used to draw the snowflake

