
new_value = input("Укажите сумму продаж:")
with open('DB_shop.txt', 'a+') as file:
    file.writelines(str(float(new_value)) + '\n')