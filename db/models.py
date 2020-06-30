from db import db_handler


class Base:
    def save(self):
        db_handler.save(self)
    @classmethod
    def select(cls,username):
        obj=db_handler.select(cls,username)
        return obj


class Admin(Base):
    def __init__(self,name,pwd):
        self.name=name
        self.pwd=pwd
        self.save()

    def create_school(self,school_name,school_address):
        School(school_name,school_address)


    def create_course(self,school_name,course_name):
        school_obj=School.select(school_name)
        school_obj.classes.append(course_name)
        school_obj.save()
        Course(school_name,course_name)

    def create_teacher(self,teacher_name):
        Teacher(teacher_name)


class School(Base):
    def __init__(self,name,address):
        self.name=name
        self.address=address
        self.classes=[]
        self.save()


class Course(Base):
    def __init__(self, school_name, name):
        self.school_name=school_name
        self.name = name
        self.class_student = []
        self.save()



class Teacher(Base):
    def __init__(self, name, pwd='666'):
        self.name = name
        self.pwd = pwd
        self.tea_course_list=[]
        self.save()
    def check_course(self):
        return self.tea_course_list
    def choice_course(self,course_name):
        self.tea_course_list.append(course_name)
        self.save()
    def check_course_student(self,course_name):
        course_obj=Course.select(course_name)
        return course_obj.class_student
    def mark(self,course_name,student_name,score):
        student_obj=Student.select(student_name)
        student_obj.stu_course_sore_dic[course_name]=score
        student_obj.save()


class Student(Base):
    def __init__(self, name, pwd):
        self.name = name
        self.pwd = pwd
        self.school=None
        self.stu_course_list = []
        self.stu_course_sore_dic = {}
        self.save()
    def choice_school(self,school_name):
        self.school=school_name
        self.save()
    def choice_course(self,course_name):
        self.stu_course_list.append(course_name)
        self.stu_course_sore_dic.update({course_name:0})
        self.save()


