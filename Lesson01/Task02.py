# 2. Пользователь вводит время в секундах. Переведите время в часы, минуты и секунды и выведите в формате чч:мм:сс.
# Используйте форматирование строк.

users_secs = int(input("Введите количество секунд, а программа посчитает количество часов, минут, и секунд>>>"))

hours = users_secs // 3600
minutes = (users_secs - (hours * 3600)) // 60
seconds = users_secs - (hours * 3600) - (minutes * 60)

print(f"Итого: {users_secs} секунд = {hours} часов, {minutes} минут и {seconds} секунд")
