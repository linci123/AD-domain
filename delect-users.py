from asyncio.log import logger
from ldap3 import Connection, Server,ALL, MODIFY_ADD, MODIFY_REPLACE, SUBTREE, ALL_ATTRIBUTES, ALL_OPERATIONAL_ATTRIBUTES
import ldap3
import pinyin

#server-conifg
server_ip = '192.168.2.201'
ldap_search_base = 'ou=淘宝科技有限公司,dc=tb,dc=com'
admin_user = 'TB\Administrator111'
admin_password = '030699Tbo'

server = Server('ldaps://'+server_ip, get_info=ALL)
ldap_conn = Connection(server, user='TB\Administrator',password='030699Tbo',read_only=False,fast_decoder=True,check_names=True,auto_bind=True)

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



def delete_users(username):
    #删除用户
    if group =='':
        group_dn = ''
    else:
        group_dn = 'ou='+group+','
    user_dn = 'cn=' + username +',' +group_dn+ ldap_search_base
    hanzi_pinyin = pinyin.get(username)
    print("\n\n\n===================开始删除用户========================")
    user_dn = 'cn=' + user +',' + ldap_search_base
    ldap_conn.delete(user_dn)
    res = ldap_conn.result
    print(user, "success")
    print("===================删除用户完毕========================")