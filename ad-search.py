from asyncio.log import logger
from ldap3 import Connection, Server,ALL, MODIFY_ADD, MODIFY_REPLACE, SUBTREE, ALL_ATTRIBUTES, ALL_OPERATIONAL_ATTRIBUTES
import ldap3
import pinyin
import csv

#server-conifg
server_ip = '192.168.2.201'
ldap_search_base = 'ou=淘宝科技有限公司,dc=tb,dc=com'
admin_user = 'TB\Administrator111'
admin_password = '030699Tbo'
path_csv = 'C:\\Users\\tb\\Desktop\\批量添加名单.csv'


server = Server('ldaps://'+server_ip, get_info=ALL)
ldap_conn = Connection(server, user='TB\Administrator',password='030699Tbo',read_only=False,fast_decoder=True,check_names=True,auto_bind=True)

#连接AD域
def connect_ldap():
    print(server.info)
    print(ldap_conn.user)
    print(ldap_conn.extend.standard.who_am_i())
print("==============================测试连接==============================")
try:
    if connect_ldap !=0:
        print('连接信息如下：')
        print(ldap_conn)
        print('=========================AD域控制器连接成功=========================')
    else:
        print('=========================AD域控制器连接失败=========================')
except Exception as e:
    logger.error('LDAP Connection: ' + str(e))
    print('请检查账号或密码是否正确')
    print('=========================AD域控制器连接失败=========================')

def search_user(username,group):
    # 查询 LDAP 用户信息
    try:
        print("\n\n\n===================开始查询用户信息========================")
        with open(path_csv, 'r',encoding='utf-8-sig') as f:
            reader = csv.reader(f)
            for row in reader:
                username = row[0]
                group = row[1]
                print(username,group)

                #判断组是否填写，
                if username == '' and group =='':
                    group_dn = ''
                    user_dn = ldap_search_base
                elif username == ''and group != '':
                    group_dn = 'ou=' + group + ','
                    user_dn = group_dn + ldap_search_base
                elif username != '' and group =='':
                    user_dn = 'cn=' + username + ldap_search_base
                else:
                    group_dn = 'ou=' + group + ','
                    user_dn = 'cn=' + username +',' +group_dn+ ldap_search_base
                hanzi_pinyin = pinyin.get(username,group)
                search_result = ldap_conn.search(
                    search_base= user_dn,
                    search_filter='(objectclass=user)',
                    search_scope=SUBTREE,
                    attributes=['distinguishedName','userPrincipalName','displayName','sAMAccountName']
                )
                
                if not search_result:
                    print(search_result, '查询失败，账号或用户组不存在，请检查输入的用户名和用户组')
                    return True
                print(search_result,'查询成功，信息如下')
                response = ldap_conn.response[0]
                # 字符串, CN=员工姓名-员工编号,OU=直属组织,OU=上层组织,OU=上上层组织,,OU=企业名称,OU=行政组织,OU=OU,DC=DC,DC=DC
                dn = response.get('dn', '')
                # 字典, {'cn': '员工姓名-员工编号', 'givenName': '员工名称', 'sAMAccountName': '员工账户名', 'mail': '员工邮箱'}
                attributes = response.get('attributes', {})
                print(attributes)
                print("===================查询用户信息完毕========================")
        return True
    except Exception as e:
        logger.error('LDAP Search: ' + str(e))
        return False

search_user(username='',group='')