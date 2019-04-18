"""
Сортировка подсчетом.count_sort
Однопроходный алгоритм
Если известно что сортируемое множество состоит из ограниченного набора различных символов
то определив эти символы например цифры от 0-9 можно последовательно подавая на вход
значения множества увеличивать значение для соответствующего индекса.
вывод отсортированного списка в файл
"""
import os
with open(os.path.join(r'C:\Users\akrylov\pyt\sorts','n_sort_big_mass.txt'),'r') as file:
    lst_file=list(map(int,(file.read().strip().split())))
F=[0] * 10
for i in lst_file:
    F[i]+=1
with open(os.path.join(r'C:\Users\akrylov\pyt\sorts','big_sort.txt'), 'w') as out_fl:
  for n in range(len(F)):
    print(str(n)*F[n],file=out_fl, end ='')