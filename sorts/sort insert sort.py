"""
Код для сортировки вставками получаемой из файла строки
Движение осуществляется справа на лево,логически список
можено разделить на отсортированную левую и не отсортированную правую части.
крайний левый элемент с индексом (hi-1 или  z-1) (на первой итерации это элем с индексом[0])
считается отсортированным до момента появления() нового
элемента справа с индексом(hi читать "z"),после чего последовательно значения элементов левее hi
сравниваются со значением элемента с убывающим индексом (hi со здвигом
через переменную "z"), если значение элемента в позиции "z" меньше значения элем. в поз "z-1"
выполняет обмен значениями, движение осуществляется до [0] элемента соответствующего на последнем шаге [z-1].
"""
import os
#list_for_sort=[]
with open(os.path.join(r'C:\Users\akrylov\pyt\sorts','non_sort_mass.txt'),'r') as imp_file:
   #list_for_sort=(str(k).strip().split(' ') for k in imp_file)
   #list_for_sort=list(k.strip().split() for k in imp_file)
   list_for_sort=list(map(int,(imp_file.read().strip().split())))
     #for k in imp_file:
      #   list_for_sort.append(str(k).split(' '))
N=len(list_for_sort)
for hi in range(1,N):
    z=hi
    while z > 0 and list_for_sort[z] < list_for_sort[z-1]:
        list_for_sort[z],list_for_sort[z-1]=list_for_sort[z-1],list_for_sort[z]
        z-=1

print(list_for_sort)