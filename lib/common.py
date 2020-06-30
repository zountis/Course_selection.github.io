





def printing_keep_of_quit(flag,msg):
    while True:
        if flag:
            print(msg)
            choice=input('输入q返回，输入其他继续: ').strip()
            if choice=='q':
                return True
            else:
                break
        else:
            print(msg)
            choice=input('输入q返回，输入其他继续: ').strip()
            if choice=='q':
                return True
            else:
                break


def login_auth(role):
    from core import admin, student, teacher
    def auth(func):
        def wrapper(*args, **kwargs):
            if role == 'admin':
                if admin.login_user.get('user'):
                    res = func(*args, **kwargs)
                    return res
                else:
                    admin.login()
            elif role == 'student':
                if student.login_user.get('user'):
                    res = func(*args, **kwargs)
                    return res
                else:
                    student.login()
            elif role == 'teacher':
                if teacher.login_user.get('user'):
                    res = func(*args, **kwargs)
                    return res
                else:
                    teacher.login()
        return wrapper
    return auth
