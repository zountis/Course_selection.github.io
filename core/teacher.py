from interface import common_interface,teacher_interface
from lib import common

login_user={
    'user':None
}



def login():
    while True:
        name = input('请输入用户名: ').strip()
        pwd = input('请输入密码: ').strip()
        flag, msg = common_interface.login_interface(name, pwd, 'teacher')
        if flag:
            print(msg)
            login_user['user'] = name
            break
        else:
            print(msg)
            break


@common.login_auth('teacher')
def check_course():
    msg=teacher_interface.check_course(login_user.get('user'))
    print(msg)


@common.login_auth('teacher')
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
            print('学校编号不存在!,请重新输入')
            continue
        course_name = course_list[choice1]
        flag, msg = teacher_interface.choice_course_interface(login_user.get('user', ), course_name)
        if flag:
            print(msg)
            break
        else:
            print(msg)
            break

@common.login_auth('teacher')
def check_course_student():
    while True:
        flag,course_list=teacher_interface.check_course_interface(login_user.get('user', ))
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
        course_name = course_list[choice1]
        flag,student_list = teacher_interface.course_student_interface(login_user.get('user'), course_name)
        print(student_list)


@common.login_auth('teacher')
def mark():
    while True:
        flag, course_list = teacher_interface.check_course_interface(login_user.get('user'))
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
        course_name = course_list[choice1]
        flag, student_list = teacher_interface.course_student_interface(login_user.get('user'), course_name)
        if not flag:
            print(student_list)
            break
        for index, student in enumerate(student_list):
            print(f'学生编号: {index}   学生名称: {student}')
        choice2 = input('请输入学生编号: ').strip()
        if not choice2.isdigit():
            print('必须输入数字！')
            continue
        choice2 = int(choice2)
        if choice2 not in range(len(course_list)):
            print('学生编号不存在!,请重新输入')
            continue
        student_name = student_list[choice2]
        score=input('请输入学生所得分数:').strip()
        if not score.isdigit():
            print('必须输入数字！')
            continue
        flag,msg=teacher_interface.mark_interface(
            login_user.get('user'),
            course_name,
            student_name,
            score
        )
        if flag:
            print(msg)
            break
        else:
            print(msg)
            break










func_dic={
    '1':login,
    '2':check_course,
    '3':choice_course,
    '4':check_course_student,
    '5':mark
}

def teacher_view():
    while True:
        print(
            '===老师===\n'
            '1  登录\n'
            '2  查看教授课程\n'
            '3  选择教授课程\n'
            '4  查看课程下学生\n'
            '5  修改分数\n'
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


