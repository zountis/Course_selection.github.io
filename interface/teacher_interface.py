from db import models



def check_course(username):
    teacher_obj=models.Teacher.select(username)
    return teacher_obj.check_course()


def choice_course_interface(username, course_name):
    taacher_obj = models.Teacher.select(username)
    if course_name in taacher_obj.tea_course_list:
        return False, f'老师[{username}]已经选择过课程[{course_name}]'
    taacher_obj.choice_course(course_name)
    return True, f'课程选择成功，老师[{username}]新选了教授课程课程[{course_name}]'



def course_student_interface(username, course_name):
    teacher_obj=models.Teacher.select(username)
    student_list=teacher_obj.check_course_student(course_name)
    if not student_list:
        return False, f'课程[{username}]还没有学生选择'
    return  True,student_list

def check_course_interface(username):
    teacher_obj = models.Teacher.select(username)
    course_list=teacher_obj.check_course()
    if not course_list:
        return False, f'老师[{username}]还没有选择任何课程'
    return True,course_list



def mark_interface(username,course_name,student_name,score):
    student_obj=models.Student.select(student_name)
    student_score=student_obj.stu_course_sore_dic.get(course_name)
    if student_score!=0:
        return False,f'你已经为该学生打过分了,打分成功，学生：[{student_name}]   得分:[{student_score}]'
    teacher_obj=models.Teacher.select(username)
    teacher_obj.mark(course_name,student_name,score)
    return False, f'打分成功，学生：[{student_name}]   得分:[{score}]'