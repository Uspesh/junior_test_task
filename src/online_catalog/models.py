from django.db import models

class Employee(models.Model):
    full_name = models.CharField(max_length=255, verbose_name='ФИО')
    work_status = models.CharField(max_length=100, verbose_name='Должность')
    start_work_time = models.TimeField(auto_now=True, verbose_name='День приема на работу')
    salary = models.IntegerField(verbose_name='Зар. Плата')
    boss = models.CharField(verbose_name='Начальник', max_length=50)
