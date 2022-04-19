#----------------1------------------
list_ip = list()
with open('nginx_logs.txt', 'r') as file:
    while True:
        line = file.readline()
        if not line:
            break
        temp_list_str = line.strip().split('"')
        ip = temp_list_str[0].split(" ")[0]
        method = temp_list_str[1].split(" ")[0]
        url = temp_list_str[1].split(" ")[1]
        list_ip.append((ip, method, url))
print(list_ip)

#----------------3-------------------------

# Не понял как сделать, посомтрю в следующем уроке как делать в разборе ДЗ

# ------------6-----------------------


