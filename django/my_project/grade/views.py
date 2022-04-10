from django.db.models import Sum, Max, Min, Avg
from django.shortcuts import render

from grade.models import Grade, Student


def page_grade(request):
    """ 学生成绩的统计 """
    # 练习1：求某个学生期末成绩的总和
    grade_list = Grade.objects.filter(student_name='张三')
    student = grade_list.aggregate(total_score=Sum('score'))
    print(student)
    # 练习2：求某一科目成绩的最高分/最低分
    # 练习3：求某一科目成绩的平均分
    subject = Grade.objects.filter(subject_name='语文').aggregate(
        max=Max('score'),
        min=Min('score'),
        avg=Avg('score'),
    )
    # 练习4：求每个学生期末成绩的总和
    stu_list = Student.objects.annotate(total=Sum('stu_grade__score'))

    return render(request, 'page_grade.html', {
        'student': student,
        'subject': subject,
        'stu_list': stu_list
    })