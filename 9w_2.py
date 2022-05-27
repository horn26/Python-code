#!/usr/bin/env python
# coding: utf-8

# In[30]:


import platform
import csv
import matplotlib.pyplot as plt
import matplotlib.font_manager as fm

june = []
july = []
aug = []
sept = []
dec = []
jan = []
feb = []

summerMonth = [june,july,aug,sept,'06','07','08','09']
winterMonth = [dec,jan,feb,'12','01','02']

summerList = []
winterList = []

year_aug = []
year_jan = []

#여름 평균 기온 함수-----------------------------------------------------------
def summerTemp(num):
    f = open('daegu_1970_2018.csv', encoding='euc_kr')
    data = csv.reader(f)
    header = next(data)
    
    for row in data:
        if row[-1] != '':
            if row[0].split('-')[1] == summerMonth[num+4]:
                summerMonth[num].append(float(row[-1]))
    sum = 0
    result = 0
                
    for temp in summerMonth[num]:
        sum += temp

    result = sum/len(summerMonth[num])
    summerList.append(result)
    
    f.close()
#겨율 평균 기온 함수-----------------------------------------------------------
def winterTemp(num):
    f = open('daegu_1970_2018.csv', encoding='euc_kr')
    data = csv.reader(f)
    header = next(data)
    
    for row in data:
        if row[-2] != '':
            if row[0].split('-')[1] == winterMonth[num+3]:
                winterMonth[num].append(float(row[-2]))
    sum = 0
    result = 0
                
    for temp in winterMonth[num]:
        sum += temp

    result = sum/len(winterMonth[num])
    winterList.append(result)
    
    f.close()
#구동부-----------------------------------------------------------
for i in range(4):
    summerTemp(i)
    if i<3:
        winterTemp(i)
#출력부-----------------------------------------------------------
print("여름철 평균 기온:")
for i in range(4):
    print("%s 월 평균 기온: %.2f"%(summerMonth[i+4],summerList[i]))
print("대구에서 가장 더운 달은 %s 월이고, 평균기온은 %.2f 도 였습니다."%(summerMonth[6],summerList[2]))

print("\n겨울철 평균 기온:")
for i in range(3):
    print("%s 월 평균 기온: %.2f"%(winterMonth[i+3],winterList[i]))
print("대구에서 가장 추운 달은 %s 월이고, 평균기온은 %.2f 도 였습니다."%(winterMonth[4],winterList[1]))
#그래프 출력-----------------------------------------------------------
f = open('daegu_1970_2018.csv', encoding='euc_kr')
data = csv.reader(f)
header = next(data)

for row in data:
    if row[-1] != '':
        if row[0].split('-')[1] == summerMonth[6]:
            syear = row[0].split('-')[0]
            year_aug.append(syear)
        elif row[0].split('-')[1] == winterMonth[4]:
            wyear = row[0].split('-')[0]
            year_jan.append(wyear)
        
f.close()
        
if platform.system() == 'Windows':
    font_name = fm.FontProperties(fname="c:\Windows\Fonts\malgun.ttf").get_name()
    plt.rc('font',family=font_name)
    
plt.figure(figsize=(25, 6))
plt.plot(year_aug, aug,'r,-',label="8월")
plt.plot(year_jan, jan, 'b,-',label="1월")
plt.title("대구의 폭염/혹한 50년사",size=16)
plt.legend(loc=5)
plt.show()

