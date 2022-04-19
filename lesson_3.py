#______________________________задание 1 и 2___________________________
def num_translate(num_en):
    translate_dic = {
        "zero": "ноль",
        "one": "один",
        "two": "два",
        "three": "три",
        "four": "четыре",
        "five": "пять",
        "six": "шесть",
        "seven": "семь",
        "eight": "восемь",
        "nine": "девять",
        "ten": "десять"
    }
    if num_en.istitle():
        return translate_dic.get(num_en.lower()).title() if translate_dic.get(num_en.lower()) is not None else None
    return translate_dic.get(num_en.lower())


print(num_translate('Zero'))
print(num_translate('six'))
print(num_translate('Zero2'))

#______________________________задание 3___________________________
list_name = ["Иван", "Мария", "Петр", "Илья", "маша"]
def get_keys(list_data):
    keys_list = []
    for item in list_data:
        keys_list.append(item[0].upper())
    return keys_list


def filter_key_list(key, filter_list):
    result_list = []
    for item in filter_list:
        if item[0].title() == key:
            result_list.append(item.title())
    return result_list

def thesaurus(*args):
    list_name = []
    result = {}
    list_name.extend(args)
    keys_list = get_keys(list_name)
    for key in keys_list:
        result[key] = filter_key_list(key, list_name)
    print(result)
    print(keys_list)
    print(list_name)


thesaurus(*list_name)

#______________________________задание 5___________________________


def get_jokes(n=1, is_only=False):
    import random
    result = []
    nouns = ["автомобиль", "лес", "огонь", "город", "дом"]
    adverbs = ["сегодня", "вчера", "завтра", "позавчера", "ночью"]
    adjectives = ["веселый", "яркий", "зеленый", "утопичный", "мягкий"]
    while n != 0:
        if nouns == [] and adverbs == [] and adjectives == []:
            # Проверяю, если слов больше не осталось то добавить в конец сообщение, что шуток больше нет и выхожу из цикла
            result.append("Шутки кончились")
            n = 0
        elif is_only:
            # Проверяю если слова в шутках не должны повторятся то полученные рандомные слова убираю из списков.
            noun = random.choice(nouns)
            nouns.remove(noun)
            adverb = random.choice(adverbs)
            adverbs.remove(adverb)
            adjective = random.choice(adjectives)
            adjectives.remove(adjective)
            result.append(f'{noun} {adverb} {adjective}')
            n -= 1
        else:
            #Если слова могут повторятся то просто вывожу рандомные слова n раз
            result.append(f'{random.choice(nouns)} {random.choice(adverbs)} {random.choice(adjectives)}')
            n -= 1
    return result


print(get_jokes(3))
print(get_jokes(8, True))
print(get_jokes())
