from DataProcessing import *
import matplotlib
import matplotlib.pyplot as plt
import numpy as np

# 中文乱码和坐标轴负号处理。
matplotlib.rc('font', family='SimHei', weight='bold')
Nowday = str(datetime.date.today())
# 开发人员Bug Reopen率
def reOpenRateplot(productId=3):
    Dev_data = reOpenRate(productId)
    # 按照reOpenRate排序
    Dev_data.sort(key=lambda k:(k.get('reOpenRate',0)),reverse=True)
    # X轴
    labels = list()
    for label in Dev_data:
        labels.append(label['name'])
    # Y轴
    reOpenRateList = list()
    for rate in Dev_data:
        reOpenRateList.append(rate['reOpenRate'])

    # 中文乱码的处理，rcParams也可以用于设置图的分辨率，大小等信息
    plt.rcParams['font.sans-serif'] =['SimHei']
    # 设置图表风格
    plt.style.use('ggplot')
    #绘图
    plt.bar(labels,reOpenRateList,0.4,color='r', alpha= 0.65)
    # 设置title
    plt.title('开发人员Bug Reopen率')
    plt.legend()
    # 数据标签
    for x,y in enumerate(reOpenRateList):
        plt.text(x,y,'%s'%'{:.2%}'.format(y), ha='center', va='bottom')
    
    s = Nowday + "-reOpen.png"
    plt.savefig(s)
    plt.show()

# 每日新增Bug数
def newBugEverDay():
    EverDayData = everDayNewBug()
    # Y轴
    labels = list()
    for label in EverDayData:
        labels.append(label['openedDate'])
    # X轴
    EverDayCountList = list()
    for everDayC in EverDayData:
        EverDayCountList.append(everDayC['everDayCount'])
    # 设置图表风格
    plt.style.use('ggplot')
    y_day = np.arange(len(labels))
    #绘图
    fig, ax = plt.subplots()
    b = ax.barh(y_day,EverDayCountList,align='center',color='#6699CC')
    #为横向水平的柱图右侧添加数据标签
    for rect in b:
        w = rect.get_width()
        ax.text(w,rect.get_y()+rect.get_height()/2, '%d' %
            int(w), ha='left', va='center')
    
    ax.set_yticks(y_day)
    ax.set_yticklabels(labels)
    ax.invert_yaxis()  # labels read top-to-bottom
    ax.set_title('每日新增Bug数')
    
    s = Nowday + "-newBugEverDay.png"
    plt.savefig(s)
    plt.show()

newBugEverDay()