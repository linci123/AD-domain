from inspect import Attribute
import logging
from tkinter import N
from ldap3 import Connection, Server,ALL, MODIFY_ADD, MODIFY_REPLACE, SUBTREE, ALL_ATTRIBUTES, ALL_OPERATIONAL_ATTRIBUTES
import pinyin
logger = logging.getLogger(__name__)

LDAP_SERVER_HOST = Server('ldaps://192.168.2.201',use_ssl=True,get_info=ALL)
LDAP_SEARCH_BASE = 'ou=淘宝科技有限公司,dc=tb,dc=com'
LDAP_USERNAME = 'TB\Administrator11'
LDAP_PASSWORD = '030699Tbo'

class LDAPVerify:
    def __init__(self):
        self.ldap_host = LDAP_SERVER_HOST
        self.ldap_search_base = LDAP_SEARCH_BASE
        self.ldap_user = LDAP_USERNAME
        self.ldap_pwd = LDAP_PASSWORD

    def connect_ldap(self):
        # 与 LDAP 建立连接
        try:
            print("==============================测试连接==============================")
            self.ldap_conn = Connection(
                self.ldap_host,
                user=self.ldap_user,
                password=self.ldap_pwd,
                auto_bind=True,
                read_only=False,
                fast_decoder=True,
                check_names=True
            )

            if self.ldap_conn ==0:
                print('=========================AD域控制器连接成功=========================')
                print(self.ldap_conn)
            else:
                print('=========================AD域控制器连接失败=========================')
            return True
        except Exception as e:
            logger.error('LDAP Connection: ' + str(e))
            return False

    def search_user(self, search_name):
        # 查询 LDAP 用户信息
        try:
            print("\n\n\n===================开始查询用户信息========================")
            search_result = self.ldap_conn.search(
                search_base= search_name+','+self.ldap_search_base,
                search_filter='(objectclass=user)',
                search_scope=SUBTREE,
                attributes=['distinguishedName','userPrincipalName']
            )
            
            if not search_result:
                print(search_result, '查询失败，请检查输入的用户名和用户组')
                return True
            print(search_result,'查询成功，信息如下')
            self.response = self.ldap_conn.response[0]
            # 字符串, CN=员工姓名-员工编号,OU=直属组织,OU=上层组织,OU=上上层组织,,OU=企业名称,OU=行政组织,OU=OU,DC=DC,DC=DC
            self.dn = self.response.get('dn', '')
            # 字典, {'cn': '员工姓名-员工编号', 'givenName': '员工名称', 'sAMAccountName': '员工账户名', 'mail': '员工邮箱'}
            self.attributes = self.response.get('attributes', {})
            print(self.attributes)
            print("===================查询用户信息完毕========================")
            return True
        except Exception as e:
            logger.error('LDAP Search: ' + str(e))
            return False

    def check_user_pwd(self, user,password):
        # 验证 LDAP 用户密码
        try:
            print("===================验证LDAP用户密码========================")
            ldap_conn_check = Connection(
                self.ldap_host,
                user=user,
                password=password,
                check_names=True,
                lazy=False,
                raise_exceptions=False
            )
            ldap_conn_check.bind()
            self.check_description = ldap_conn_check.result['description']
            return True
        except Exception as e:
            logger.error('LDAP Check: ' + str(e))
            return False


            
    def add_users(self,user):
        print("\n\n\n===================开始添加用户========================")
        # 添加用户
        user_dn = 'cn=' + user +',' + self.ldap_search_base
        att={
        #用户名
        'displayName':user,
        #设置登录密码
        # 'userPassword': '123456Tbo',
        #用户登录名
        'userPrincipalName': user+'@tb.com',
        #用户登录名
        'sAMAccountName':user
            }
        self.ldap_conn.add(user_dn,object_class=['organizationalPerson', 'person', 'top', 'user'],attributes=att)
        #激活用户
        # self.ldap_conn.extend.microsoft.modify_Password(user_dn,new_passwd='12346Tbo')
        self.ldap_conn.extend.microsoft.modify_password(user_dn,new_password="12346Tbo")
        self.ldap_conn.modify(user_dn,{'userAccountControl':[(MODIFY_REPLACE,[512])]})
        res = self.ldap_conn.result
       
        print(res)
        # # 用户已存在
        # if res['result'] != 0:
        #     msg = res['description']
        #     print("add user failed:%s      res: %s" % (user, res))
        # res = self.ldap_conn.result
        # msg = "success"
        # if res['result'] != 0:
        #     msg = res['message']
        #     print("add user to group:%s                  res: %s" % (msg))
        # print(user, "success")
        print("===================添加用户完毕========================")



    def delete_users(self,user):
        #删除用户
        print("\n\n\n===================开始删除用户========================")
        user_dn = 'cn=' + user +',' + self.ldap_search_base
        self.ldap_conn.delete(user_dn)
        res = self.ldap_conn.result
        print(user, "success")
        print("===================删除用户完毕========================")


    def main(self, search_name, password):
        # LDAP 验证主方法
        if not self.connect_ldap():
            return False, {'message': 'Failed to establish connection with LDAP'}
        if not self.search_user(search_name):
            return False, {'message': 'Failed to query LDAP user information'}
        if not self.response:
            return False, {'message': 'No LDAP user information found'}
        if not self.check_user_pwd(password):
            return False, {'message': 'Unable to verify LDAP user password'}
        if not self.check_description == 'success':
            return False, {'message': 'User name and password do not match'}
        return True, {'dn': self.dn, 'attributes': self.attributes}
# def ldap_user_auth(username, password):
#     v = LDAPVerify()
#     state, result = v.main(username, password)

ldapverify = LDAPVerify()
ldapverify.connect_ldap()
# ldapverify.search_user(search_name='cn=李四,ou=开发组')
# ldapverify.main(search_name="HAIXUN\Administrator",password='123456Tbo')
# ldapverify.check_user_pwd(password="123456Tbo")
# ldapverify.delete_users(user="RD100")
# ldapverify.add_users(user="RD113")


