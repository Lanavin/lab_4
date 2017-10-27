import random


# Генератор вычленения полей из массива словарей
# Пример:
# goods = [
#    {'title': 'Ковер', 'price': 2000, 'color': 'green'},
#    {'title': 'Диван для отдыха', 'price': 5300, 'color': 'black'}
# ]
# field(goods, 'title') должен выдавать 'Ковер', 'Диван для отдыха'
# field(goods, 'title', 'price') должен выдавать {'title': 'Ковер', 'price': 2000}, {'title': 'Диван для отдыха', 'price': 5300}

def field(items, *args):
    assert len(args) > 0
    # Необходимо реализовать генератор (итерируемый объект, но прочитать можно лишь 1 раз)
    if len(args) == 1:
        for i in items:
            for key in args:
                a = i.get(key)
                if a is not None:
                    yield a #вернуть значение а
    else:
        for i in items:
            dict = {}
            for key in args:
                a = i.get(key)
                if a is not None:
                    dict[key] = a
            if len(dict) > 0:
                yield dict
# Генератор списка случайных чисел
# Пример:
# gen_random(1, 3, 5) должен выдать примерно 2, 2, 3, 2, 1
# Hint: реализация занимает 2 строки
def gen_random(begin, end, num_count):
    for i in range(num_count):
        yield random.randint(begin, end)