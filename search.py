from random import randint as ri
 #Создание списка случайными числами
start_list = []
for i in range(0,100): 
    start_list.append(ri(0, 1_000_000))
unsorted_list = start_list
sorted_list = []
#Сортировка этого списка
while len(unsorted_list) > 0:
    min = unsorted_list[0]
    for i in range(0, len(unsorted_list)):
        if unsorted_list[i] < min:
            min = unsorted_list[i]
    sorted_list.append(min)
    unsorted_list.remove(min)
#Вывод исходного списка
print('Исходный список:')
print(sorted_list)
#Ввод искомого числа
print('Введите число, которое следует найти')
x=int(input())
#Линейный поиск
count_1=0
for i in range(len(sorted_list)): 
    if sorted_list[i] == x:
        break
    count_1+=1
if sorted_list[i] != x:
    print('Элемент не найден')
else:
    print('Индекс элемента, найденный алгоритмом "Линейный поиск" =',i)
print('Количество сравнений =',count_1)
print(' ')
#Бинарный поиск
count_2=0
first = 0
last = len(sorted_list)-1
index = -1
while (first <= last) and (index == -1): 
    mid = (first+last)//2
    if sorted_list[mid] == x:
        index = mid
    else:
        if x<sorted_list[mid]:
            last = mid -1
        else:
            first = mid +1
    count_2+=1
if index == -1:
    print('Элемент не найден')
else:
    print('Индекс элемента, найденный алгоритмом "Бинарный поиск" =',index)
print('Количество сравнений =',count_2)