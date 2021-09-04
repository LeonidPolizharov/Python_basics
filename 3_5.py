
def get_jokes(cnt, flag=False):
    """
    Генерирует шутки, случайным образом составленные из слов, в количестве, указанном пользователем,
    с возможностью вывода уникальных слов
    :param cnt: - количество выводимых шуток
    :param flag: - флаг уникальности слов, по умолчанию False (неуникальные слова)
    :return: - возвращает список шуток
    """
    import random
    nouns = ["автомобиль", "лес", "огонь", "город", "дом"]
    adverbs = ["сегодня", "вчера", "завтра", "позавчера", "ночью"]
    adjectives = ["веселый", "яркий", "зеленый", "утопичный", "мягкий"]
    i = 0
    jokes = []
    if not flag:
        while i < cnt:
            jokes.append(f"{random.choice(nouns)} {random.choice(adverbs)} {random.choice(adjectives)}")
            i += 1
    elif 0 < cnt <= len(nouns):
        while i < cnt:
            noun = random.choice(nouns)
            adverb = random.choice(adverbs)
            adjective = random.choice(adjectives)
            jokes.append(f"{noun} {adverb} {adjective}")
            nouns.remove(noun)
            adverbs.remove(adverb)
            adjectives.remove(adjective)
            i += 1
    else:
        return(print(f"Для уникальных шуток их кол-во может быть не более {len(nouns)}-и"))
    return print(jokes)


get_jokes(cnt=4, flag=True)

