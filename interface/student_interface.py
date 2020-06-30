from db import models


def register_interface(username, pwd):
    student_obj = models.Student.select(username)
    if student_obj:
        return False, f'学生[{username}]已存在'
    models.Student(username, pwd)
    return True, f'注册成功，新增学生[{username}]'


def choice_school_interface(username,school_name):
    student_obj=models.Student.select(username)
    if student_obj.school:
        return False, f'学生[{username}]已经选择过学校了，所属学校为[{student_obj.school}]'
    student_obj.choice_school(school_name)
    return True, f'学校选择成功，学生[{username}]所属学校为[{school_name}]'


def choice_course_interface(username,course_name):
    student_obj=models.Student.select(username)

    if course_name in student_obj.stu_course_list:
        return False, f'学生[{username}]已经选择过课程[{course_name}]'
    student_obj.choice_course(course_name)
    course_obj=models.Course.select(course_name)
    course_obj.class_student.append(username)
    course_obj.save()
    return True, f'课程选择成功，学生[{username}]新选课程[{course_name}]'


def check_score_interface(username):
    student_obj=models.Student.select(username)
    return student_obj.stu_course_sore_dic