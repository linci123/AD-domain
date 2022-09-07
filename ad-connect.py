from asyncio.log import logger
from http import server
from unicodedata import name
from unittest import result
from ldap3 import Connection, Server,ALL, MODIFY_ADD, MODIFY_REPLACE, SUBTREE, ALL_ATTRIBUTES, ALL_OPERATIONAL_ATTRIBUTES
import ldap3
import logging


#server-conifg
server_ip = '192.168.2.201'
admin_user = 'TB\Administrator111'
admin_password = '030699Tbo'



#连接AD域
def connect_ldap():
    try:
        print("==============================测试连接==============================")
        host = Server('ldaps://192.168.2.201', get_info=ALL)
        ldap_conn = Connection(
            host, 
            user=admin_user,
            password=admin_password,
            read_only=False,
            fast_decoder=True,
            check_names=True,
            auto_bind=True
            )
            #通过是否接收到返回信息判断域控是否连接

        if ldap_conn !=0:
            print(ldap_conn)
            print('=========================AD域控制器连接成功=========================')
        else:
            print('=========================AD域控制器连接失败=========================')
        return True
    except Exception as e:
        logger.error('LDAP Connection: ' + str(e))
        print('请检查账号或密码是否正确')
        print('=========================AD域控制器连接失败=========================')
        return False
print(connect_ldap())
# if __name__=='__main__':
#     result_ldap = connect_ldap() 
#     print(result_ldap())