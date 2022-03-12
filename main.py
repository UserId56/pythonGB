#---------------------------Задание 1--------------------------
# duration = 400153
# result = ''
# Time_dictionary = [
#     {
#         'title': 'дней',
#         'time': 86400
#     },
#     {
#         'title': 'часов',
#         'time': 3600
#     },
#     {
#         'title': 'минут',
#         'time': 60
#     },
#     {
#         'title': 'секунд',
#         'time': 1
#     }
# ]
# for item in Time_dictionary:
#     temp_duration = duration // item['time']
#     if temp_duration != 0:
#         result = f'{result} {str(temp_duration)} {item["title"]}'
#         duration = duration % item['time']
# print(result)
#
# #---------------------------Задание 2--------------------------
# list_number = []
# sum_numbers_seven = 0
# for number_item in range(1, 1001, 2):
#     coub_number = number_item**3
#     list_number.append(coub_number)
#     temp_summ = 0
#     for number_element in str(coub_number):
#         temp_summ += int(number_element)
#     if temp_summ % 7 == 0:
#         sum_numbers_seven += coub_number
# print(sum_numbers_seven)
# print(list_number)
# sum_numbers_seven = 0
# for i in range(0, len(list_number)):
#     list_number[i] += 17
#     temp_summ = 0
#     for number_element in str(list_number[i]):
#         temp_summ += int(number_element)
#     if temp_summ % 7 == 0:
#         sum_numbers_seven += list_number[i]
# print(sum_numbers_seven)
# print(list_number)
# #---------------------------Задание 3--------------------------
# for i in range(1, 100):
#     number_ten = i // 10
#     number_last = i % 10
#     if number_ten == 1:
#         print(i, ' процентов')
#     elif number_last == 1:
#         print(i, ' процент')
#     elif number_last == 2 or number_last == 3 or number_last == 4:
#         print(i, ' процента')
#     else:
#         print(i, ' процентов')
#_______Lesson 2________________
#______________________________задание 1___________________________

print(type(15 * 3))
print(type(15 / 3))
print(type(15 // 2))
print(type(15 ** 2))

#______________________________задание 2 and 3___________________________
l = ['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+5', 'градусов']
is_final = True
i = 0
result = ''
while is_final:
    if not l[i].isalpha():
        if int(l[i]) // 10 == 0:
            l_width = 2 if len(l[i]) == 1 else 3
            l[i] = l[i].zfill(l_width)
        l = l[0:i] + ['"', l[i], '"'] + l[i+1:len(l)]
        i += 3
    else:
        i += 1
    if i == len(l):
        is_final = False
is_first = True
for item in l:
    if item != '"' and item.isalpha():
        result += item + " "
    else:
        result += item if is_first or (not item.isalpha() and item != '"') else item + " "
        is_first = not is_first if item == '"' else is_first
print(result)
#______________________________задание 4___________________________
user_list = ['инженер-конструктор Игорь', 'главный бухгалтер МАРИНА', 'токарь высшего разряда нИКОЛАй', 'директор аэлита']
for user_data in user_list:
    user_name = user_data.split()[-1].title()
    print(f'Привет, {user_name}')
#______________________________задание 5___________________________

price = [56.1, 32, 31.7, 127, 432.1, 670, 35, 76.5, 1, 2.7]
result_str = ''
for item_price in price:
    temp_list_price = str(item_price).split('.')
    if len(temp_list_price) < 2:
        rub = temp_list_price[0] + " руб " if len(temp_list_price[0]) > 1 else temp_list_price[0].zfill(2) + " руб "
        result_str += rub + "00 коп, "
    else:
        rub = temp_list_price[0] + " руб " if len(temp_list_price[0]) > 1 else temp_list_price[0].zfill(2) + " руб "
        cop = temp_list_price[1] + " коп, " if len(temp_list_price[1]) > 1 else temp_list_price[1].zfill(2) + " коп, "
        result_str += rub + cop
print(result_str)
print(sorted(price))
print(price)
sort_price = sorted(price, reverse=True)
print(sort_price)
print(sorted(sort_price[0:5]))