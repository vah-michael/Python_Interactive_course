# 1. Создать список и заполнить его элементами различных типов данных.
#   Реализовать скрипт проверки типа данных каждого элемента.
#   Использовать функцию type() для проверки типа.
#   Элементы списка можно не запрашивать у пользователя, а указать явно, в программе.

first_list=[1,2,3,4]

new_list = [1, 1.2, "строка", (10<5), first_list]
max_index_count = len(new_list)

index_count = 0
while index_count <= max_index_count-1:
    print(type(new_list[index_count]))
    index_count += 1
