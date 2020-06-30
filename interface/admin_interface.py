from db import models



def register_interface(username,pwd):
    admin_obj=models.Admin.select(username)
    if admin_obj:
        return False,f'管理员[{username}]已存在'
    models.Admin(username,pwd)
    return True,f'注册成功，新增管理员[{username}]'


def create_school_interface(username,school_name,school_address):
    school_obj = models.School.select(school_name)
    if school_obj:
        return False, f'学校[{school_name}]已存在'
    admin_obj = models.Admin.select(username)
    admin_obj.create_school(school_name,school_address)
    return True, f'学校创建成功，新增学校[{school_name}]'


def create_course_interface(username,school_name,course_name):
    school_obj = models.School.select(school_name)
    if not school_obj:
        return False, f'学校[{school_name}]不存在'
    if course_name in school_obj.classes:
        return False, f'学校[{school_name}]已存在课程[{course_name}]'
    admin_obj = models.Admin.select(username)
    admin_obj.create_course(school_name, course_name)
    return True, f'课程创建成功，学校[{school_name}]新增学校[{course_name}]'


def create_teacher_interface(username,teacher_name):
    teacher_obj = models.Teacher.select(teacher_name)
    if teacher_obj:
        return False, f'老师[{teacher_name}]已存在'
    admin_obj = models.Admin.select(username)
    admin_obj.create_teacher(teacher_name)
    return True, f'老师创建成功，新增老师[{teacher_name}]，初始密码:666'
