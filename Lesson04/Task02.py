# 2. Представлен список чисел. Необходимо вывести элементы исходного списка, значения которых больше предыдущего элемента.
# Подсказка: элементы, удовлетворяющие условию, оформить в виде списка. Для формирования списка использовать генератор.
# Пример исходного списка: [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55].
# Результат: [12, 44, 4, 10, 78, 123].

my_list = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]
new_list = []
count_my_list = 0

def new_list_former (curr_number):
        if curr_number < my_list[count_my_list]:
            new_list.append(my_list[count_my_list])

for curr_number in my_list:
    if count_my_list < len(my_list)-1:
        count_my_list += 1
        new_list_former(curr_number)

print(my_list)
print(new_list)
