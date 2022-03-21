# 3. Узнайте у пользователя число n. Найдите сумму чисел n + nn + nnn.
# Например, пользователь ввёл число 3. Считаем 3 + 33 + 333 = 369.

users_number = input("Введите число n, а программа посчитает сумму чисел n + nn + nnn>>>")
first_number = int(users_number)
second_number = int(f"{first_number}{first_number}")
third_number = int(f"{first_number}{first_number}{first_number}")

summ_numbers = first_number + second_number + third_number

print("Сумма чисел по схеме n + nn + nnn:")
print(f"{first_number} + {second_number} + {third_number} = {summ_numbers}")