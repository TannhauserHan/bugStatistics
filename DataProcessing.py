from bugStatistics_Sql import *
import datetime

fixedGreaterOne = []
resolvedBugCount = []
result = []
Nowday = str(datetime.date.today())

def reOpenRate():
    return ""

def userList():
    user_list = []
    for res in list(connect_db(bugSql.sql_dev())):
        user_list.append(res['account'])
    return user_list

fixedGreaterOne = list(connect_db(bugSql.sql_fixedGreaterOne_bug_count(3)))
resolvedBugCount = connect_db(bugSql.sql_resolved_bug_count(3))
    #day = datetime.datetime.strftime(res['openedDate'],'%Y-%m-%d')
    # 获取当前时间
    #if Nowday==day :
    #    print(True)
Dev_list = list()
Dev_dict = dict()
index = 0

for dictResolve in resolvedBugCount:
    for dictFix in fixedGreaterOne:
        if dictResolve['resolvedBy']==dictFix['resolvedBy']:
            Dev_dict['name'] = dictFix['realname']
            #Dev_dict['fixedGreaterOneCount'] = dictFix['fixedGreaterOneCount']
            #Dev_dict['resolvedBugCount'] = dictResolve['resolvedBugCount']
            Dev_dict['reOpenRate'] = '{:.2%}'.format(dictFix['fixedGreaterOneCount']/dictResolve['resolvedBugCount'])
            print(Dev_dict['name'],Dev_dict['reOpenRate'])
            Dev_list.append(Dev_dict)  

for dictResolve in resolvedBugCount:
    while(index<len(fixedGreaterOne)):
        if dictResolve['resolvedBy']== fixedGreaterOne[index]['resolvedBy']:
            Dev_dict['name'] = dictResolve['realname']
            #Dev_dict['fixedGreaterOneCount'] = dictFix['fixedGreaterOneCount']
            #Dev_dict['resolvedBugCount'] = dictResolve['resolvedBugCount']
            Dev_dict['reOpenRate'] = '{:.2%}'.format(fixedGreaterOne[index]['fixedGreaterOneCount']/dictResolve['resolvedBugCount'])
            print(Dev_dict['name'],Dev_dict['reOpenRate'])
            index  = index + 1
            Dev_list.append(Dev_dict)
        break

for res in Dev_list:
    print(res)

        