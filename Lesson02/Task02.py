# 2. Для списка реализовать обмен значений соседних элементов,
# т.е. Значениями обмениваются элементы с индексами 0 и 1, 2 и 3 и т.д.
# При нечетном количестве элементов последний сохранить на своем месте.
# Для заполнения списка элементов необходимо использовать функцию input().

new_list = []
first_elem = input("Введите первый элемент списка(любое значение)>>>")
new_list.append(first_elem)

index_count = 0
while True:
    index_count += 1
    new_element = input("Введите следующий элемент списка. Для завершения ввода элемента списка введите (выход)")
    if new_element == "выход" or new_element == "Выход":
        first_list = new_list
        break
    else:
        new_list.append(new_element)

print("Первый список",first_list)

new_index_count = 1
max_index_count = len(new_list)

while True:
    even_element_bystep = new_list[new_index_count-1]
    no_even_element_bystep = new_list[new_index_count]
    new_list[new_index_count] = even_element_bystep
    new_list[new_index_count-1] = no_even_element_bystep
    new_index_count += 2


    if new_index_count >= max_index_count:
       second_list = new_list
       break

print("Второй список",second_list)