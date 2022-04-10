import threading

from django.db.models import F

from grade.models import Grade

"""
UPDATE `grade` SET `student_id` = 1, `student_name` = '张三', `subject_name` = '语文', `score` = 800, `year` = 2000 
WHERE `grade`.`id` = 1; args=(1, '张三', '语文', 800.0, 2000, 1)


UPDATE `grade` SET `student_id` = 1, `student_name` = '张三', `subject_name` = '语文', `score` = (`grade`.`score` + 1), `year` = 2000 WHERE `grade`.`id` = 1; args=(1, '张三', '语文', 1, 2000, 1)
"""


class ChangeThread(threading.Thread):
    """ 改变分数 """

    def __init__(self, max_count=1000, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.max_count = max_count

    def run(self):
        count = 0
        grade_obj = Grade.objects.get(pk=1)
        while True:
            # 最多循环max_count次
            if count >= self.max_count:
                break

            print(self.getName(), count)
            # grade_obj.score += 1
            grade_obj.score = F('score') + 1
            grade_obj.save()
            count +=1


def main():
    t1 = ChangeThread(max_count=800, name='T1')
    t2 = ChangeThread(max_count=500, name='T2')
    t1.start()
    t2.start()
    t1.join()
    t2.join()
