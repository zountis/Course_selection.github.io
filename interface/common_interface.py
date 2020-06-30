from db import models
from conf import settings
import os



def login_interface(username, pwd,role):
    if role=='admin':
        obj = models.Admin.select(username)
    elif role=='student':
        obj = models.Student.select(username)
    elif role=='teacher':
        obj = models.Teacher.select(username)
    else:
        return False,'输入的角色不存在，请联系管理员'
    if not obj:
        return False, '用户不存在'
    elif pwd !=obj.pwd:
        return False, '密码不正确'
    return True, f'[{role}: {username}],登录成功'


def get_all_school():
    user_dir = os.path.join(settings.DATA_PATH,'School')
    if not os.path.exists(user_dir):
        return False, '没有任何学校，请联系管理员'
    return True,os.listdir(user_dir)

def get_school_course(school_name):
    school_obj=models.School.select(school_name)
    course_list=school_obj.classes
    if not course_list:
        return False,f'学校[{school_name}]没有任何课程，请联系管理员'
    return True,course_list

