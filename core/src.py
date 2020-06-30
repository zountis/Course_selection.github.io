from core import admin,teacher,student







func_dic={
    '1':admin.admin_view,
    '2':student.student_view,
    '3':teacher.teacher_view
}




def run():
    while True:
        print(
    '===老男孩教育===\n'
    '1  管理员界面\n'
    '2  学生界面\n'
    '3  老师界面\n'
    '======end======')
        choice=input('请输入界面编号(输入q退出系统): ').strip()
        if choice=='q':
            break
        if not choice.isdigit():
            print('请输入数字')
            continue
        if choice not in func_dic:
            print('输入的编号不存在,请重新输入')
            continue
        func_dic.get(choice)()
