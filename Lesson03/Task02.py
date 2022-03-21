# 2. Реализовать функцию, принимающую несколько параметров, описывающих данные пользователя:
#   имя, фамилия, год рождения, город проживания, email, телефон.
#   Функция должна принимать параметры как именованные аргументы.
#   Реализовать вывод данных о пользователе одной строкой.

def user_profile(first_name, last_name, birth_year, home_city, e_mail, phone):
    print(
        f"{first_name} {last_name}. "
        f"Год рождения: {birth_year}. "
        f"Город проживания: {home_city}. "
        f"Е:mail: {e_mail}. "
        f"Телефон: {phone}")


first_name = input("Введите имя пользователя>>>")
last_name = input("Введите фамилию пользователя>>>")
birth_year = int(input("Введите год рождения>>>"))
home_city = input("Введите город проживания>>>")
e_mail = input("Введите адрес электронной почты>>>")
phone = input("Введите телефон пользователя>>>")

user_profile(first_name, last_name, birth_year, home_city, e_mail, phone)
