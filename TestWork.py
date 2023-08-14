import json
import codecs
import datetime
import re

fs = codecs.open("competitors2.json", "r", "utf-8")
fr = open("results_RUN.txt", "r")
d = json.loads(fs.read())
lst = dict()
for s in fr.readlines():
    st = s.rstrip('\n').split(' ')
    iter = re.findall(r'\d+',st[0])[0]
    if(st[1] == 'start'):
        d[iter]['time'] = datetime.datetime.strptime(st[2], '%H:%M:%S,%f')
    else:
        d[iter]['time'] = datetime.datetime.strptime(st[2], '%H:%M:%S,%f') - d[iter]['time'] 
        lst[iter] = d[iter]
del d
fs.close()
fr.close()
sorted_d = sorted(lst.items(), key=lambda x: x[1].get('time'))
print('| Занятое место | Нагрудный номер | Имя | Фамилия | Результат |\n| --- | --- | --- | --- | --- |')
cnt = int(1)
for i in sorted_d:
    print('| ' + str(cnt) + ' | ' + i[0] + ' | ' + i[1].get('Name') + ' | ' + i[1].get('Surname') + ' | ' + str(i[1].get('time')) + ' |')
    cnt += 1
del sorted_d
del lst