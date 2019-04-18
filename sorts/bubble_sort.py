""" Сортировка методом пузырька
Сортировка выполняется слева направо
в случае если значение левого элемент больше
значения правого элемента выполняется обмен значениями
причем после каждого прохода свою позицию будет занимать наибольший элемент из
неотсортированных поэтому ходить до последеней позиции каждый раз не нужно
"""
import os
with open(os.path.join(r'C:\Users\akrylov\pyt\sorts','non_sort_mass.txt'),'r') as import_file:
    list_for_sort=list(map(int,(import_file.read().strip().split())))
N=len(list_for_sort)
for iteration in range(1,N):
    for x in range(0,N-iteration):
        if list_for_sort[x] > list_for_sort[x+1]:
            list_for_sort[x],list_for_sort[x+1]=list_for_sort[x+1],list_for_sort[x]
print(list_for_sort)