# 4. Пользователь вводит целое положительное число. Найдите самую большую цифру в числе.
# Для решения используйте цикл while и арифметические операции.


user_number = int(input("Введите положительное число>>>"))
while user_number < 0:
    user_number = int(input("Вы вводите отрицательное число. Введите положительное число>>>"))
else:
    str_number = f"{user_number}"
    max_digit_count = len(str_number)
    max_digit = str_number[0]

digit_count = 0
while True:
        digit_count += 1
        if digit_count == max_digit_count:
            print("Количество цифр в числе:", max_digit_count)
            print("Максимальная цифра в числе:", max_digit)
            break

        elif str_number[digit_count] > max_digit:
            max_digit = str_number[digit_count]
