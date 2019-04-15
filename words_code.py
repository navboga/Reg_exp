import os
st=('')
apl_fl = open(os.path.normpath(r'C:\Users\7YA\Desktop\python\dataset_3363_2.txt '), 'r')
foolstring=str(apl_fl.readline().strip())
dgt=('')
abc=('')
fin=('')
apl_fl.close()
for i in range(0,len(foolstring),1):
    if foolstring[i].isdigit():
      dgt+=foolstring[i]
    else :
      abc+=foolstring[i]
      if len(dgt)>0:
        dgt+='.'
new_dgt=list(dgt.split('.'))
for x in range(len(abc)):
  fin+=abc[x]*int(new_dgt[x])
download_file = open(os.path.normpath(r'C:\Users\7YA\Desktop\python\dataset_3363_2_result.txt '), 'w')
download_file.write(fin)
download_file.close()

