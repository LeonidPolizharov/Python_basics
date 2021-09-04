def num_translate_adv(income_num):
    num_dict = {'zero': 'ноль', 'one': 'один', 'two': 'два', 'three': 'три', 'four': 'четыре', 'five': 'пять',
                'six': 'шесть', 'seven': 'семь', 'eight': 'восемь', 'nine': 'девять', 'ten': 'десять'}
    if income_num[0].isupper():
        transl = num_dict.get(income_num.lower()).capitalize()
    else:
        transl = num_dict.get(income_num.lower())
    return print(transl)


num_translate_adv(input('Введите число на английском: '))
