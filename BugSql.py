from datetime import datetime

class bugSql:
    # 每天新增Bug数
    @staticmethod
    def sql_new_bug_everDay(productId):
            return "select count(openedDate) as everDayCount,openedDate from zt_bug where deleted = '0' and product = %s group by %s"%(productId,"date_format(openedDate,'%Y-%m-%d')")
    
    # 每天解决Bug数
    @staticmethod
    def sql_resolved_bug_everDay(productId):
        return "select count(resolvedDate) as bugCount,resolvedDate from zt_bug where deleted = '0' and status <> 'active' and resolution <> 'postponed' and product = %s group by %s" %(productId,"date_format(resolvedDate,'%Y-%m-%d')")
    
    # 今天的新增bug数
    @staticmethod
    def sql_active_bug_nowDay(productId):
        return "select count(*) as bugCount,assignedTo from zt_bug where deleted = '0' and status = 'active' and %s<=assignedDate and product = %s group by assignedTo" %("DATE_FORMAT(CURDATE(),'%Y-%m-%d %H:%i:%s')",productId)
    
    # 每天新增Bug数(还未关闭的)
    @staticmethod
    def sql_notColsed_bug_everDay(productId):
        return "select count(openedDate) as EverDayNewBugCount,openedDate from zt_bug where deleted = '0' and product = %s and status <> 'closed' group by %s" %(productId,"date_format(openedDate,'%Y-%m-%d')")

    # 开发人员已解决的Bug数
    @staticmethod
    def sql_resolved_bug_count(productId):
        return "select count(*) as resolvedBugCount,resolvedBy from zt_bug where resolution = 'fixed' and product =%s and resolvedBy in (select account from zt_user where deleted = '0' and visits >= 5 and `role` not in ('qa','po','pm','pd') and account <> 'admin')group by resolvedBy" %(productId)
    
    # 开发人员未能一次解决Bug的次数
    @staticmethod
    def sql_fixedGreaterOne_bug_count(productId):
        return "select count(*) as fixedGreaterOneCount,resolvedBy from zt_bug where resolution = 'fixed' and activatedCount > 0 and product = %s and resolvedBy in (select account from zt_user where deleted = '0' and visits >= 5 and `role` not in ('qa','po','pm','pd') and account <> 'admin')group by resolvedBy" %(productId)

    # 查询开发人员
    @staticmethod
    def sql_dev():
        return "select account,realname from zt_user where deleted = '0' and visits >= 5 and `role` not in ('qa','po','pm','pd') and account <> 'admin'"
