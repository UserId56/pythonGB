def get_duct(tutors, klasses):
    for i in range(len(tutors)):
        yield (tutors[i], klasses[i] if i<len(klasses) else None)

tutors = [
    'Иван', 'Анастасия', 'Петр', 'Сергей',
    'Дмитрий', 'Борис', 'Елена'
]
klasses = [
    '9А', '7В', '9Б', '9В', '8Б', '10А', '10Б', '9А'
]
klasses2 = [
    '9А', '7В'
]
generator = get_duct(tutors, klasses2)
print(next(generator))
print(next(generator))
print(next(generator))
print(next(generator))
print(next(generator))
print(next(generator))
print(next(generator))
print(next(generator))

#---------------задние 4 ----------------------
def get_num_list(num_list):
    for num in num_list:
        yield num

src = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]
tem_prev_num = src[0]
generator_num = get_num_list(src)
result = []

for i in range(1, len(src)):
    if src[i] > tem_prev_num:
        result.append(src[i])
    tem_prev_num = src[i]
print(result)

src = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]


def generator_src(src_list):
    for item in src_list:
        yield item

generator_init = generator_src(src)
result = []
for i in range(len(src)):
    item_search = next(generator_init)
    if src.count(item_search) == 1:
        result.append(item_search)

print(result)