import csv
#open('temp_ice.csv', 'r')
f=open('temp_ice.csv', 'r', encoding='euc-kr')
data=csv.reader(f)
header=next(data)
temp=[]
ice=[]
#전체 데이터 행별로 저장 및 출력
for row in data:
    temp.append(float(row[1]))
    ice.append(int(row[4]))
    
print(temp)
print(ice)

print("\n\n\n--------------------------------------------------------------------------\n\n\n")
print(min(temp), max(temp))
print("\n\n\n--------------------------------------------------------------------------\n\n\n")


import numpy as np

bins=np.arange(min(temp), max(temp)+5, 5)
print(bins)

print("\n\n\n--------------------------------------------------------------------------\n\n\n")

hist, bins=np.histogram(temp, bins)
print(hist)
print(bins)

print("\n\n\n--------------------------------------------------------------------------\n\n\n")
ice_buy = np.zeros(9)
for i in range(0,len(temp)):
    if bins[0] <= temp[i] and temp[i] <bins[1]:
        ice_buy[0] = ice_buy[0] + ice[i]
    elif bins[1] <=temp[i] and temp[i] <bins[2]:
        ice_buy[1] = ice_buy[1] + ice[i]
    elif bins[2] <=temp[i] and temp[i] <bins[3]:
        ice_buy[2] = ice_buy[2] + ice[i]    
    elif bins[3] <=temp[i] and temp[i] <bins[4]:
        ice_buy[3] = ice_buy[3] + ice[i]
    elif bins[4] <=temp[i] and temp[i] <bins[5]:
        ice_buy[4] = ice_buy[4] + ice[i]
    elif bins[5] <=temp[i] and temp[i] <bins[6]:
        ice_buy[5] = ice_buy[5] + ice[i]
    elif bins[6] <=temp[i] and temp[i] <bins[7]:
        ice_buy[6] = ice_buy[6] + ice[i]
    elif bins[7] <=temp[i] and temp[i] <bins[8]:
        ice_buy[7] = ice_buy[7] + ice[i]
    else:
        ice_buy[8] = ice_buy[8] + ice[i]
    
print(ice_buy)

print("\n\n\n-------------------------------------------------------------\n\n\n")

ice_buy_a=np.zeros(9)

for i in range(0, len(ice_buy)):
    ice_buy_a[i]=ice_buy[i]/hist[i]
for i in range(0, len(ice_buy)):
    print('%0.2f' % ice_buy_a[i])
    
import matplotlib.pyplot as plt 
plt.xlabel('Average temperature')
plt.ylabel('Number of ice cream shopping')
plt.bar(bins[0:9],ice_buy_a,width=2, align ='edge')
plt.xticks(bins[0:9])
plt.show()

print("\n\n\n-------------------------------------------------------------\n\n\n")


plt.scatter(temp,ice)
plt.show()
