from random import randint, choice

def random_koch_func():
    data = [str(randint(5, 20)), str(randint(30, 180)),
             str(randint(30, 180)), str(randint(30, 180)),
             str(randint(2, 20))]
    return data

def random_l_func():
    rnd_path = ''
    rnd_list = ['F', 'S', '+', '-', '[', ']']
    for rule in range(randint(5, 20)):
        rnd_path += choice(rnd_list)

    data = [rnd_path, str(randint(1, 5)), 
            str(randint(5, 20)), str(randint(30, 120))]
            
    return data

    