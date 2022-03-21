#4. Пользователь вводит строку из нескольких слов, разделённых пробелами.
# Вывести каждое слово с новой строки. Строки необходимо пронумеровать.
# Если в слово длинное, выводить только первые 10 букв в слове.

print("Программа разделяет строку пользователя из нескольких слов.")
print("Каждое слово в новой пронумерованной строке (длина слова не больше 10 символов.")

user_string = input("Введите строку из нескольких слов>>>")

elem_count = 1
while True:
    delim_user_string = user_string.find(" ")
    if delim_user_string != -1:
        new_element = user_string[:delim_user_string]
        user_string = user_string.replace(f"{new_element} ", "")
        print(f"{elem_count}. {new_element[:10]}")
        elem_count += 1

    if delim_user_string == -1:
        print(f"{elem_count}. {user_string[:10]}")
        break





# Велосипедистка проезжается по Шарикодшипниковской улице