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
    Dev_name = list()
    for label in Dev_data:
        Dev_name.append(label['name'])
    # Y轴
    # Bug Reopen率
    reOpenRateList = list()
    for rate in Dev_data:
        reOpenRateList.append(rate['reOpenRate'])
    # 开发人员未能一次解决Bug的次数
    fixedGreaterOneCountList = list()
    for fix in Dev_data:
        fixedGreaterOneCountList.append(fix['fixedGreaterOneCount'])
    # 开发人员已解决的Bug数
    resolvedBugCountList = list()
    for resolved in Dev_data:
        resolvedBugCountList.append(resolved['resolvedBugCount'])
    
    # 中文乱码的处理，rcParams也可以用于设置图的分辨率，大小等信息
    plt.rcParams['font.sans-serif'] =['SimHei']
    # 设置图表风格
    plt.style.use('ggplot')
    #绘图
    #plt.bar(Dev_name,reOpenRateList,0.4,color='r', alpha= 0.65)
    plt.bar(Dev_name,reOpenRateList,0.4,color='r', alpha= 0.65)
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
    #plt.show()

def Demo(productId=3):
    Dev_data = reOpenRate(productId)
    #按照reOpenRate排序
    #Dev_data.sort(key=lambda k:(k.get('reOpenRate',0)),reverse=True)
    # X轴
    Dev_name = list()
    for label in Dev_data:
        Dev_name.append(label['name'])
    # Y轴
    # Bug Reopen率
    reOpenRateList = list()
    for rate in Dev_data:
        reOpenRateList.append('{:.2%}'.format(rate['reOpenRate']))
        #reOpenRateList.append((rate['reOpenRate'])
    # 开发人员未能一次解决Bug的次数
    fixedGreaterOneCountList = list()
    for fix in Dev_data:
        fixedGreaterOneCountList.append(fix['fixedGreaterOneCount'])
    # 开发人员已解决的Bug数
    resolvedBugCountList = list()
    for resolved in Dev_data:
        resolvedBugCountList.append(resolved['resolvedBugCount'])
    
    # 中文乱码的处理，rcParams也可以用于设置图的分辨率，大小等信息
    plt.rcParams['font.sans-serif'] =['SimHei']
    # 设置图表风格
    plt.style.use('ggplot')
    x = np.arange(len(Dev_name))
    width = 0.35

    fig, ax = plt.subplots()
    rects1 = ax.bar(x - width/2, fixedGreaterOneCountList, width, label='开发人员未能一次解决Bug的次数')
    rects2 = ax.bar(x + width/2, resolvedBugCountList, width, label='开发人员已解决的Bug数')
    ax.set_xticks(x)
    ax.set_xticklabels([])
    ax.legend()

    ax.set_title('Bug统计')

    def autolabel(rects):
        for rect in rects:
            height = rect.get_height()
            ax.annotate('{}'.format(height),
                        xy=(rect.get_x() + rect.get_width() / 2, height),
                        xytext=(0, 3),  # 3 points vertical offset
                        textcoords="offset points",
                        ha='center', va='bottom')
    
    autolabel(rects1)
    autolabel(rects2)

    rows = ['reOpenRate']
    #print(rows)
    val3 = [['{}'.format(r) for r in reOpenRateList] for r in range(1)] 
    the_table = ax.table(cellText=val3,
                        rowLabels=rows,
                        colLabels=Dev_name,
                        loc='bottom')
    
    s = Nowday + "-Bug.png"
    plt.savefig(s)                    
    #plt.show()