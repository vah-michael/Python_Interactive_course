def my_func(new_elements, total):
    print(type(new_elements))
    new_list = new_elements.split()
    print(new_list)
    print(len(new_list))
    summ_elem = 0
    for elem in new_list:
        if elem == "q":
          return total
        else:
            elem = int(elem)
            #print(elem)
            summ_elem = summ_elem + elem

    total = total + summ_elem
    print("Сумма введенных чисел", summ_elem)
    print("Сумма всех введенных чисел", total)
    return total





#new_list = input("Введите числа через пробел. Для выхода нажмите (q)>>>")

new_list = "5 5 5 5"
total = 0
print(my_func(new_list, total))
#print(total)

#while new_list != "q":
 #   new_list = input("Введите числа через пробел. Для выхода нажмите (q)>>>")
  #  my_func(new_list, total)