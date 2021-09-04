def num_translate(income_num):
    num_dict = {'zero': 'ноль', 'one': 'один', 'two': 'два', 'three': 'три', 'four': 'четыре', 'five': 'пять',
                'six': 'шесть', 'seven': 'семь', 'eight': 'восемь', 'nine': 'девять', 'ten': 'десять'}
    transl = num_dict.get(income_num.lower())
    return print(transl)


num_translate(input('Введите число на английском: '))
