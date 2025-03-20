account = 'nihao'
password = '123456'

user_account = input('请输入账号：')
user_pasword = input('请输入密码：')

if account == user_account and password == user_pasword:
    print('登录成功')   
else:
    print('登录失败')
    