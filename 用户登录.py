#!/usr/bin/env  python
# -*- coding:utf-8 -*-
# Author:tx.shi
# 模拟登陆：
# 1. 用户输入帐号密码进行登陆
# 2. 用户信息保存在文件内
# 3. 用户密码输入错误三次后锁定用户
import getpass,sys

i = 0
while i<3:
    username = input("请输入用户名：")
    lock_list = open('lock_account.txt','r+',encoding="utf-8")
    for lock in lock_list.readlines():
        user_lock = lock.strip('\n')
        if user_lock == username:
            print("用户%s已被锁定，请联系管理员解锁！"%(username))
            sys.exit(1)
    user_list = open('account.txt','r',encoding="utf-8")
    for line in user_list.readlines():
        (user,passwd) = line.strip('\n').split(',')
        if user == username:
            j = 0
            while j < 3:
                password = input("请输入密码：")
                # password = getpass.getpass("请输入密码：")
                if passwd == password:
                    print("用户%s登录成功，欢迎光临！"%(username))
                    sys.exit(0)
                else:
                    if j != 2:
                        print("用户%s的密码错误，您还有%d次机会进行尝试！"%(username,2-j))
                j +=1
            else:
                lock_list.write(username+'\n')
                print("您尝试的次数过多，用户%s已被锁定，请联系管理员解锁！"%(username))
                sys.exit(1)
    i +=1
    if i < 3:
        print("用户%s不存在，您还有%d次机会尝试!"%(username,3-i))
else:
    print("您尝试的次数过多，请稍后再试！")
    sys.exit(1)



























'''
i = 0
while i<3:
    lock_user_list = open('lock_account.txt','r+',encoding="utf-8")
    username = input("请输入用户名：")
    for lock in lock_user_list.readlines():
        lock_user = lock.strip('\n')
        if lock_user == username:
            print("帐号已被锁定，请联系管理员解锁后再登录！")
            sys.exit(1)
    user_list = open('account.txt','r',encoding="utf-8")
    for line in user_list.readlines():
        (user,passwd) = line.strip('\n').split(',')
        if user == username:
            j = 0
            while j<3:
                # password = getpass.getpass("请输入密码：")
                password = input("请输入密码：")
                if passwd == password:
                    print("欢迎用户%s登录平台！"%(username))
                    sys.exit(0)
                else:
                    if j != 2:
                        print("用户%s的密码错误，还有%d次机会可以尝试！"%(username,2-j))
                j += 1
            else:
                print("您尝试的次数过多，用户%s已被锁定，请联系管理员解锁！"%(username))
                lock_user_list.write(username+'\n')
                sys.exit(1)
    i += 1
    if i<3:
        print("用户%s不存在，您还有%d次机会可以尝试！"%(username,3-i))
else:
    print("您尝试的次数过多，请稍后再试！")
    sys.exit(1)

'''