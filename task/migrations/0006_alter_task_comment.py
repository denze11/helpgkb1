# Generated by Django 4.0.5 on 2022-07-07 19:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('task', '0005_remove_category_abbreviation_department_abbreviation'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='comment',
            field=models.TextField(blank=True, default='', null=True, verbose_name='Комментарий'),
        ),
    ]
