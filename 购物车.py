#!/usr/bin/env  python
# -*- coding:utf-8 -*-
# Author:tx.shi
goods_list = {
             'iphone6': {'price':6000,'num':10,'sum':10},
             'ipad': {'price':3000,'num':20,'sum':20},
             'mi4': {'price':2000,'num':43,'sum':43},
             'huawei6_plus': {'price':1999,'num':8,'sum':8},
}
########################打印商品列表函数###################################

########################商品列表展示函数###################################
def goods_list_show(my_dict):

    local_dict = {}                                                        ###定义函数内部字典###
    ############对商品列表进行遍历并加上数字编号###########################
    i = 1
    print('商品列表 : ')
    print('=================================================================================')
    print('%-5s  %-20s  %-10s  %-10s  %-10s' % ('编号','商品名称','商品价格(元)','商品总数量(个)','商品剩余数量(个)'))
    for k in my_dict:
        v = my_dict[k]
        if type(v) is dict:
            print('%-5d  %-20s  %-10d  %-10d  %-10d' % (i,k,v['price'],v['sum'],v['num']))
            local_dict[i] = [k,v['price'],v['num'],v['sum']]               ###将商品列表赋值到local_dict###
        i += 1
    print('=================================================================================')

    return local_dict                                                      ###返回格式化后的字典###
goods_list_show(goods_list)