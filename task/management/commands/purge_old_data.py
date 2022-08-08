from django.core.management.base import BaseCommand
from task.models import Task
from datetime import datetime, timedelta


class Command(BaseCommand):
    help = 'Удаление объектов старше 90 дней'

    def handle(self, *args, **options):
        Task.objects.filter(date_created__lte=datetime.now() -
                            timedelta(days=90)).delete()
        self.stdout.write('Удаленные объекты старше 90 дней')

# Добавить команду в crone  на ежедневный запуск
# python /путь до файла/manage.py purge_old_data
