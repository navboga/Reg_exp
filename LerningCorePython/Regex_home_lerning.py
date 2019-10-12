import re


s = 'This and that.'
result = re.search(r'(Th\w+) and (th\w+)', s, re.I)
print(result.group())

result1 = re.search(r'(Th\w+) and (th\w+)', s, re.I)
print(result1.groups())

m = re .match ( 'foo', 'Food оn the tаblе ',re.IGNORECASE) # сопоставление выполняется успешно
print(m.group())

I=re.search(r'\bthe', 'in the ithening or ivning', re.I) #re.I - игнорирование верхенего\нижнего регистра при поиске
print(I.group(),'проверяем поиск вначале слова')

Z1= re.findall(r'dog','buldog or doghanter or Snup Dog  not cat',re.I)#findall работает как search но возвращает всегда список, либо пустой либо с элементами

print(Z1[2],'по позиции в списке')

for i in range(len(Z1)):
    print(Z1[i])



    # find=re.finditer(r' (th\w+) and (th\w+) ', s,re.I)
#
# some = find.next().groups()('Тhis', 'that')
#
#
#re.finditer(r' (th\w+) and (th\w+) ', s,re.I).next().group(l)
# #
# # re.finditer(r' (th\w+) and (th\w+) ', s,re.I).next() .group(2)
