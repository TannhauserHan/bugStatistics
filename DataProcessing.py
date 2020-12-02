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
Dev_dirct = dict()
for dirctResolve in resolvedBugCount:
    print(dirctResolve['resolvedBugCount'],dirctResolve['resolvedBy'])
    for dirctFix in fixedGreaterOne:
        if dirctResolve['resolvedBy']==dirctFix['resolvedBy']:
            Dev_dirct['name'] = dirctFix['resolvedBy']
            Dev_dirct['fixedGreaterOneCount'] = dirctFix['fixedGreaterOneCount']
            Dev_dirct['resolvedBugCount'] = dirctResolve['resolvedBugCount']