"""
Функция переводчик, которая переводит
полученные данные в целые числа
"""
def number_converter(arr):
    try:
        return list(map(int, arr))
    except (TypeError):
        return None


