本节作业

作业需求：

模拟实现一个ATM + 购物商城程序

额度 15000或自定义
实现购物商城，买东西加入 购物车，调用信用卡接口结账
可以提现，手续费5%
每月22号出账单，每月10号为还款日，过期未还，按欠款总额 万分之5 每日计息
支持多账户登录
支持账户间转账
记录每月日常消费流水
提供还款接口
ATM记录操作日志
提供管理接口，包括添加账户、用户额度，冻结账户等。。。
    因对本次作业的MVC结构没有思路，故研究分析了王松牛人的作业，现整理如下：


ATM 模拟程序说明
系统主程序为根目录下的:day5_credit_card.py
1. 系统功能模块
Day5_ATM 模拟程序是在python3.0 环境下开发



2. 系统目录结构：
程序采用分层的方式编写,包括数据库访问层、数据库层(数据文件)、业务逻辑层（module 层），业务处理层（主程序）、


3．应用知识点：
a) 字典、列表、元组的操作
b) 文件的读写操作
c) 函数的应用
d) 类的使用
e) 装饰器、反射