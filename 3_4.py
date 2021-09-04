def thesaurus_adv(*args):
    reg = {}
    print(args)
    for i in args:
        if i[i.index(" ") + 1] not in reg:
            reg.setdefault(i[i.index(" ") + 1], {i[0]: [i]})
        elif i[0] not in reg[i[i.index(" ") + 1]]:
            reg[i[i.index(" ") + 1]].update({i[0]: [i]})
        else:
            (reg[i[i.index(" ") + 1]][i[0]]).append(i)
    return print(dict(sorted(reg.items(), key=lambda x: x[0])))


thesaurus_adv("Иван Охлобыстин", "Мария Шарапова", "Петр Налич", "Илья Варламов", "Виктор Пелевин", "Елена Малышева", "Леонид Каневский", "Павел Глоба", "Максим Поташов", "Михаил Горбачев", "Игорь Крутой", "Владимир Путин")
# thesaurus_adv("Иван Сергеев", "Инна Серова", "Петр Алексеев", "Илья Иванов", "Анна Савельева")