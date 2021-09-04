def thesaurus(*args):
    reg = {}
    print(args)
    for i in args:
        if i[0] not in reg.keys():
            reg.setdefault(i[0], [i])
        else:
            reg[i[0]].append(i)
    return print(dict(sorted(reg.items(), key=lambda x: x[0])))


thesaurus("Иван", "Мария", "Петр", "Илья", "Виктор", "Елена", "Леонид", "Павел", "Максим", "Михаил")
