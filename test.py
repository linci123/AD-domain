# from http import server
# from importlib.metadata import entry_points
# import json
# import logging
# from re import search
# from tkinter import Entry
# import sys
# from ldap3 import Connection, Server, ALL, MODIFY_ADD, MODIFY_REPLACE, SUBTREE, ALL_ATTRIBUTES, ALL_OPERATIONAL_ATTRIBUTES
# import utils
import csv
# from turtle import pd


# csv_c = pd.read
with open('C:\\Users\\tb\\Desktop\\批量添加名单.csv', 'r',encoding='utf-8-sig') as f:
    reader = csv.reader(f)
    print(reader)
    for r in reader:
        print(r)

# # server = Server('192.168.2.201', get_info=ALL)
# # conn = Connection(server,'administrator', '030699Tbo',auto_bind=True)
# # server.info

# # 'cn=administrator,cn=Users,dc=tb,dc=com','030699Tbo'
# #检查连接是否成功
# def test_connection():
#     print(server.info)
#     print(conn.user)
#     print(conn.extend.standard.who_am_i())
# print("==============================测试连接==============================")
# if test_connection !=0:
#     print('=========================AD域控制器连接成功=========================')
# else:
#     print('=========================AD域控制器连接失败=========================')


# #获取用户
# def get_users():
#     conn.search(search_base="ou=淘宝科技有限公司,dc=TB,dc=com",attributes=ALL_ATTRIBUTES,search_filter='(objectclass=user)')
#     print(conn.result)
#     res = conn.response_to_json()
#     res = json.loads(res)['entries']
#     return res
# # print("\n\n\n==============================打印用户==============================")
# # print(get_users())


# ldap_config = {}

# excel_file_path = "ldap-users-example.xlsx"
# ldap_user_excel_file = excel_file_path


# # #查询用户
# # def search_users(user_dn):
# #     print("\n\n\n===================开始查询用户信息========================")
# #     # 查询用户
# #     status = conn.search(search_base=user_dn,search_filter='(objectclass=user)', attributes=['distinguishedName','userPrincipalName',search_scope=SUBTREE)
# #     # print(conn.entries)
# #     if status:
# #         print(status, "查询成功")
# #     else:
# #         print(status, "查询失败，请检查输入的用户名或用户组")
# #     print("===================查询用户信息完毕========================")
# # print(search_users(user_dn='cn=李四,ou=运维组,ou=淘宝科技有限公司,dc=tb,dc=com'))

# # conn.delete('cn=test,ou=淘宝科技有限公司,dc=tb,dc=com')
# # conn.add('cn=test,ou=淘宝科技有限公司,dc=tb,dc=com',['user', 'posixGroup', 'top'],{'givenName': 'test', 'sn': 'test', 'departmentNumber': 'DEV', 'telephoneNumber': 159})
# # print(conn.result)
# # conn.search('ou=海迅科技有限公司,dc=haixun,dc=com', '(cn=test111)', attributes=['objectClass'])



# # # 查询人员信息
# # def search_users():
# #     # 读取用户excel信息
# #     userattrs = utils.generate_ldap_userattrs(ldap_user_excel_file)
# #     # print(userattrs)

# #     print("\n\n\n===================开始查询用户信息========================")
# #     for user_dn, userattr in userattrs.items():
# #         # 查询用户
# #         print(user_dn)
# #         status = conn.search(search_base = user_dn,
# #                              search_filter = '(objectClass=inetOrgPerson)',
# #                              search_scope = SUBTREE,
# #                              attributes = ALL_ATTRIBUTES)
# #         if status:
# #             print(user_dn, "success")
# #         else:
# #             print(user_dn, "failed")
# #     print("===================查询用户信息完毕========================
# # 





