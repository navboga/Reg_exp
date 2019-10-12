import re
Z1= re.finditer(r'dog','buldog or doghanter or Snup Dog  not cat',re.I)#findall работает как search но возвращает всегда список, либо пустой либо с элементами
it=iter(Z1)
#print(it,type(it))

def return_iner (data):
    return next(data).group(),iter(data)

print(return_iner(Z1))

# for i in range(3):
#    print(next(Z1).group(), sep='\n')
