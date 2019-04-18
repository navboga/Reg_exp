"""
Код для сортировки выбором получаемой из файла строки.
Движение происходит слева направо, текущее значение в позици(pos) в списке
принимается за минимальное с которым последовательно сравниваются остальные
значения списка от pos+1 до N при выявлении значения меньшего чем хранится в
списке под индексом pos выполняется обмен значениями и значени в pos заменяется на меньшее.
Таким образом после каждого прохода в позиции pos будет стоять минимальное значение из оставшихся.
"""
import os
with open(os.path.join(r'C:\Users\akrylov\pyt\sorts','non_sort_mass.txt'),'r') as imp_file:
   list_for_sort=list(map(int,(imp_file.read().strip().split())))
N=len(list_for_sort)
for pos in range(N-1):
    for d in range(pos+1,N):
        if list_for_sort[pos] > list_for_sort[d]:
            list_for_sort[pos],list_for_sort[d]=list_for_sort[d],list_for_sort[pos]
print(list_for_sort)
