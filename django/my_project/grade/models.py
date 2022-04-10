from django.db import models


class Student(models.Model):
    """ 学生表 """
    name = models.CharField('学生的姓名', max_length=32)
    age = models.SmallIntegerField('学生年龄', default=0)

    class Meta:
        db_table = 'grade_student'


class Grade(models.Model):
    """ 学生成绩 """
    student = models.ForeignKey(Student,on_delete=models.CASCADE, null=True,
                                related_name='stu_grade')
    student_name = models.CharField('学生的姓名', max_length=32)
    subject_name = models.CharField('科目', max_length=32)
    score = models.FloatField('分数', default=0)
    year = models.SmallIntegerField('年份')

    class Meta:
        db_table = 'grade'
