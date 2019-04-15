import os
lst_values=[]
result=[]
result_sr=[]
sm=cnt_predm=sr_sm=sr_sf=sr_sl=0
with open(os.path.join(r'C:\Users\7YA\Desktop\python','dataset_3363_4.txt'), 'r') as task_file:
    for elements in task_file:
        lst_values.append( ((str(elements).lower()).strip()).split(';') )
        #lst_values+=(dict((str(elements).lower()).strip()).split(';'))
for i in range (len(lst_values)):
    sm = cnt_predm =z = 0
    for j in range(len(lst_values[i])):
        if str(lst_values[i][j]).isdigit():
            sm+=int(lst_values[i][j])
            cnt_predm+=1
        if (j % 10)==1:
            sr_sm+=int(lst_values[i][j])
        if (j % 10)==2:
            sr_sf+=int(lst_values[i][j])
        if (j % 10)==3:
            sr_sl+=int(lst_values[i][j])

    result.append(round((sm/cnt_predm),9))
result_sr.append(round(sr_sm / len(lst_values),9))
result_sr.append(round(sr_sf / len(lst_values),9))
result_sr.append(round(sr_sl / len(lst_values),9))
#{key: value for item in list if conditional}
with open(os.path.join(r'C:\Users\7YA\Desktop\python','task3_report.txt'), 'w') as repfile:
  print('\n'.join(map(str,result)),' '.join(map(str,result_sr)),sep = '\n',file=repfile)