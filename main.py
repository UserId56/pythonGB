#---------------------------Задание 1--------------------------
duration = 400153
result = ''
Time_dictionary = [
    {
        'title': 'дней',
        'time': 86400
    },
    {
        'title': 'часов',
        'time': 3600
    },
    {
        'title': 'минут',
        'time': 60
    },
    {
        'title': 'секунд',
        'time': 1
    }
]
for item in Time_dictionary:
    temp_duration = duration // item['time']
    if temp_duration != 0:
        result = f'{result} {str(temp_duration)} {item["title"]}'
        duration = duration % item['time']
print(result)

#---------------------------Задание 2--------------------------
list_number = []
sum_numbers_seven = 0
for number_item in range(1, 1000, 2):
    coub_number = number_item**3
    list_number.append(coub_number)
    temp_summ = 0
    for number_element in str(coub_number):
        temp_summ += int(number_element)
    if not temp_summ % 7:
        sum_numbers_seven += temp_summ
print(sum_numbers_seven)
print(list_number)
sum_numbers_seven = 0
for i in range(0, len(list_number)):
    list_number[i] += 17
    temp_summ = 0
    for number_element in str(list_number[i]):
        temp_summ += int(number_element)
    if not temp_summ % 7:
        sum_numbers_seven += temp_summ
print(sum_numbers_seven)
print(list_number)
#---------------------------Задание 3--------------------------
for i in range(1, 100):
    number_ten = i // 10
    number_last = i % 10
    if number_ten == 1:
        print(i, ' процентов')
    elif number_last == 1:
        print(i, ' процент')
    elif number_last == 2 or number_last == 3 or number_last == 4:
        print(i, ' процента')
    else:
        print(i, ' процентов')