#!/usr/bin/env python
"""
该模块用来定义系统的菜单模板
"""
# 主程序中的主菜单

index_default_menu = '''
-------------------------------------------------------------------------
                             ATM 模拟程序

{0}                                        今天 {1}   星期{2}
-------------------------------------------------------------------------
【1】进入商城 【2】登录系统 【3】信用卡中心 【4】后台管理 【5】退出系统
'''

# 主程序中的用户登录后的显示菜单

index_logined_menu = '''
-------------------------------------------------------------------------
                             ATM 模拟程序

{0}                                        今天 {1}   星期{2}
-------------------------------------------------------------------------
【1】进入商城 【2】用户中心 【3】信用卡中心 【4】后台管理 【5】退出系统
'''

# 主程序中的用户中心菜单

index_user_center = '''
-------------------------------------------------------------------------
                                用户中心

当前用户:{0}                                   今天 {1}   星期{2}
-------------------------------------------------------------------------
【1】修改密码 【2】修改资料 【3】我的账单 【4】购物记录 【5】注销 【6】返回

'''

# 用户中心按键对应功能模块
user_center_func = {
    "1": {"module": "modules.users", "func": "modify_password"},
    "2": {"module": "modules.users", "func": "modify_user_info"},
    "3": {"module": "modules.report", "func": "print_bill_history"},
    "4": {"module": "modules.report", "func": "print_shopping_history"},
    "5": {"module": "modules.users", "func": "logout"}
}

# 购物模块的主菜单, menu 菜单在shopping模块中内部构造

shopping_index_menu = '''
    ==================================================================================
    =                                                                                =
    =                                 信用卡购物商城                                  =
    =                                                                                =
    ==================================================================================

    {menu}
    '''

# 账单报表显示模板
report_bill = '''
------------------------------------------------------------------------------
                                 用户中心 - 账单明细

卡号:{cardno}                           账单时间:{startdate} 至 {enddate}
------------------------------------------------------------------------------
     交易时间        交易类型        交易金额           流水号
{billdetail}

'''

# 购物历史记录显示模板
shopping_history = '''
------------------------------------------------------------------------------
                                  用户中心 - 购物明细

用户:{username}                           购物时间:{startdate} 至 {enddate}
------------------------------------------------------------------------------
'''

# 后台管理模板
index_admin = '''
------------------------------------------------------------------------------
                               后台管理

用户:{username}
------------------------------------------------------------------------------
【1】创建用户               【2】删除用户         【3】解锁用户
【4】发行信用卡             【5】冻结信用卡       【0】退出后台管理
'''

# ATM 管理模块
index_ATM = '''
------------------------------------------------------------------------------
                               信用卡管理中心

卡号:{cardno}
------------------------------------------------------------------------------
【1】我的信用卡    【2】提现    【3】转账     【4】还款    【5】返回
'''

# 显示用户基本信息模板
user_info = '''
------------------------------------------------------------------------------
                               用户基本信息

用 户 名:{username}        姓    名:{name}               手    机:{mobile}
用户权限:{role}            是否锁定:{islocked}           是否删除:{isdel}
信用卡号:{bindcard}
------------------------------------------------------------------------------
'''

# 显示信用卡基本信息模板
card_info = '''
-----------------------------------------------------------------------------------
                               信用卡基本信息

卡号:{cardno}   所有人:{owner}  信用额度:{total}  剩余额度:{balance} 状态:{status}
-----------------------------------------------------------------------------------
'''
report_statement_list = '''
----------------------------------------------------------------------------------
                                信用卡对账单列表
卡号:{cardno}
----------------------------------------------------------------------------------
    账单号            还款日        应还款        已还款
{show_msg}
'''

report_statement_detail = '''
---------------------------------------------------------------------------------------
                               信用卡对账单

卡号：{cardno}                                          账单编号:{serino}
---------------------------------------------------------------------------------------
  账单日            账单日期范围              还款日       应还款     已还款     利息
{billdate}    {sdate} 至 {edate}     {pdate}    {total}     {payed}     {interest}
---------------------------------------------------------------------------------------
账单明细：
     交易时间        交易类型        交易金额           流水号
{details}
'''