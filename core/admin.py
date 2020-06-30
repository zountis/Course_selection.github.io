from interface import admin_interface,\
    teacher_interface,\
    common_interface,\
    student_interface
from lib import common



login_user={
    'user':None
}


def register():
    while True:
        name=input('请输入用户名: ').strip()
        pwd=input('请输入密码: ').strip()
        re_pwd=input('请确认密码: ').strip()
        if pwd==re_pwd:
            flag,msg=admin_interface.register_interface(name,pwd)
            flag=common.printing_keep_of_quit(flag,msg)
            if flag:
                break



def login():
    while True:
        name = input('请输入用户名: ').strip()
        pwd = input('请输入密码: ').strip()
        flag, msg = common_interface.login_interface(name, pwd,'admin')
        if flag:
            print(msg)
            login_user['user']=name
            break
        else:
            print(msg)
            break


@common.login_auth('admin')
def create_school():
    while True:
        school_name=input('请输入学校名称: ').strip()
        school_address=input('请输入学校地址: ').strip()
        flag,msg=admin_interface.create_school_interface(
            login_user.get('user'),school_name, school_address)
        flag=common.printing_keep_of_quit(flag,msg)
        if flag:
            break


@common.login_auth('admin')
def create_course():
    while True:
        school_name = input('请输入课程所属学校名称: ').strip()
        course_name = input('请输入课程名: ').strip()
        flag, msg = admin_interface.create_course_interface(
            login_user.get('user'), school_name, course_name)
        flag = common.printing_keep_of_quit(flag, msg)
        if flag:
            break


@common.login_auth('admin')
def create_teacher():
    while True:
        teacher_name = input('请输入老师姓名: ').strip()
        flag, msg = admin_interface.create_teacher_interface(
            login_user.get('user'), teacher_name)
        flag = common.printing_keep_of_quit(flag, msg)
        if flag:
            break





func_dic={
    '1':register,
    '2':login,
    '3':create_school,
    '4':create_course,
    '5':create_teacher
}

def admin_view():
    while True:
        print(
            '===管理员===\n'
            '1  注册\n'
            '2  登录\n'
            '3  创建学校\n'
            '4  创建课程\n'
            '5  创建老师\n'
            '======end======')
        choice = input('请输入功能编号(输入q返回): ').strip()
        if choice == 'q':
            break
        if not choice.isdigit():
            print('请输入数字')
            continue
        if choice not in func_dic:
            print('输入的编号不存在,请重新输入')
            continue
        func_dic.get(choice)()
