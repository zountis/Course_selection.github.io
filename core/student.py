from interface import common_interface,student_interface
from lib import common


login_user={
    'user':None
}
def register():
    while True:
        name = input('请输入用户名: ').strip()
        pwd = input('请输入密码: ').strip()
        re_pwd = input('请确认密码: ').strip()
        if pwd == re_pwd:
            flag, msg = student_interface.register_interface(name, pwd)
            flag = common.printing_keep_of_quit(flag, msg)
            if flag:
                break


def login():
    while True:
        name = input('请输入用户名: ').strip()
        pwd = input('请输入密码: ').strip()
        flag, msg = common_interface.login_interface(name, pwd, 'student')
        if flag:
            print(msg)
            login_user['user'] = name
            break
        else:
            print(msg)
            break

@common.login_auth('student')
def choice_school():
    while True:
        flag,school_list=common_interface.get_all_school()
        if not flag:
            print(school_list)
            break
        for index,school in enumerate(school_list):
            print(f'学校编号: {index}   学校名称: {school}')
        choice=input('请输入学校编号: ').strip()
        if not choice.isdigit():
            print('必须输入数字！')
            continue
        choice=int(choice)
        if choice not in range(len(school_list)):
            print('学校编号不存在!,请重新输入')
            continue
        school_name=school_list[choice]
        flag,msg=student_interface.choice_school_interface(login_user.get('user'),school_name)
        if flag:
            print(msg)
            break
        else:
            print(msg)
            break



@common.login_auth('student')
def choice_course():
    while True:
        flag, school_list = common_interface.get_all_school()
        if not flag:
            print(school_list)
            break
        for index, school in enumerate(school_list):
            print(f'学校编号: {index}   学校名称: {school}')
        choice = input('请输入学校编号: ').strip()
        if not choice.isdigit():
            print('必须输入数字！')
            continue
        choice = int(choice)
        if choice not in range(len(school_list)):
            print('学校编号不存在!,请重新输入')
            continue
        school_name = school_list[choice]
        flag, course_list = common_interface.get_school_course(school_name)
        if not flag:
            print(course_list)
            break
        for index, course in enumerate(course_list):
            print(f'课程编号: {index}   课程名称: {course}')
        choice1 = input('请输入课程编号: ').strip()
        if not choice1.isdigit():
            print('必须输入数字！')
            continue
        choice1 = int(choice1)
        if choice1 not in range(len(course_list)):
            print('课程编号不存在!,请重新输入')
            continue
        course_name=course_list[choice1]
        flag, msg = student_interface.choice_course_interface(login_user.get('user'),course_name)
        if flag:
            print(msg)
            break
        else:
            print(msg)
            break


@common.login_auth('student')
def check_score():
    msg=student_interface.check_score_interface(login_user.get('user'))
    print(msg)






func_dic={
    '1':register,
    '2':login,
    '3':choice_school,
    '4':choice_course,
    '5':check_score
}

def student_view():
    while True:
        print(
            '===学生===\n'
            '1  注册\n'
            '2  登录\n'
            '3  选择学校\n'
            '4  选择课程\n'
            '5  查看分数\n'
            '====end====')
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
