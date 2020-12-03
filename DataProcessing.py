from bugStatistics_Sql import *
import datetime

# day = datetime.datetime.strftime(res['openedDate'],'%Y-%m-%d')
# 获取当前时间
# if Nowday==day :
# print(True)
# Nowday = str(datetime.date.today())

def reOpenRate(productId):
    Dev_list = list()
    index = 0
    fixedGreaterOne = connect_db(bugSql.sql_fixedGreaterOne_bug_count(productId))
    resolvedBugCount = connect_db(bugSql.sql_resolved_bug_count(productId))
    for dictResolve in resolvedBugCount:
        while(index<len(fixedGreaterOne)):
            if dictResolve['resolvedBy']== fixedGreaterOne[index]['resolvedBy']:
                Dev_dict = dict()
                Dev_dict['name'] = dictResolve['realname']
                Dev_dict['fixedGreaterOneCount'] = fixedGreaterOne[index]['fixedGreaterOneCount']
                Dev_dict['resolvedBugCount'] = dictResolve['resolvedBugCount']
                #Dev_dict['reOpenRate'] = '{:.2%}'.format(fixedGreaterOne[index]['fixedGreaterOneCount']/dictResolve['resolvedBugCount'])
                Dev_dict['reOpenRate'] = fixedGreaterOne[index]['fixedGreaterOneCount']/dictResolve['resolvedBugCount']
                #print(Dev_dict['name'],Dev_dict['reOpenRate'])
                index  = index + 1
                Dev_list.append(Dev_dict)
                break
            else:
                Dev_dict = dict()
                Dev_dict['name'] = dictResolve['realname']
                Dev_dict['fixedGreaterOneCount'] = fixedGreaterOne[index]['fixedGreaterOneCount']
                Dev_dict['resolvedBugCount'] = dictResolve['resolvedBugCount']
                #Dev_dict['reOpenRate'] = '{:.2%}'.format(0/dictResolve['resolvedBugCount'])
                Dev_dict['reOpenRate'] = 0/dictResolve['resolvedBugCount']
                #print(Dev_dict['name'],Dev_dict['reOpenRate'])
                Dev_list.append(Dev_dict)
                break
    return Dev_list

        