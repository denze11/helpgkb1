from django.db import models
from django.urls import reverse
from task.models import Department


class ItYear(models.Model):
    department = models.ForeignKey(
        Department, verbose_name='Подразделение', on_delete=models.CASCADE)
    description = models.TextField('Описание')
    initiator = models.CharField('Инициатор', max_length=250)
    performer = models.CharField(
        'Исполнитель', max_length=250, blank=True, null=True, default='',)
    phone_number = models.CharField('Номер телефона', max_length=250)
    date_completed = models.DateTimeField(
        'Дата завершения', auto_now=False, blank=True, null=True)
    date_created = models.DateTimeField('Дата создания', auto_now_add=True,)
    completed = models.BooleanField('Завершить', default=False)
    comment = models.TextField(
        'Комментарий', blank=True, null=True, default='')

    def __str__(self):
        return str(self.department)

    def get_absolute_url(self):
        return reverse('it_tasks')

    class Meta:
        verbose_name = 'Заявка'
        verbose_name_plural = 'Заявки'
