from DataProcessing import *
import matplotlib
import matplotlib.pyplot as plt

Dev_data = reOpenRate(3)

labels = list()
reOpenRateList = list()
for label in Dev_data:
    labels.append(label['name'])

for rate in Dev_data:
    reOpenRateList.append(rate['reOpenRate'])

print(labels)
print(reOpenRateList)

# 中文乱码的处理，rcParams也可以用于设置图的分辨率，大小等信息
plt.rcParams['font.sans-serif'] =['SimHei']
#plt.rcParams['axes.unicode_minus'] = False

plt.bar(labels,reOpenRateList,0.3,color='r', alpha= 0.8)

plt.xlabel("开发人员")
#plt.ylabel('BugReopen率')

plt.title('开发人员Bug Reopen率')
plt.legend()
#plt.xticks(range(len(labels)),labels)

for x,y in enumerate(reOpenRateList):
    plt.text(x,y,'%s'%'{:.2%}'.format(y), ha='center', va='bottom')

plt.show()