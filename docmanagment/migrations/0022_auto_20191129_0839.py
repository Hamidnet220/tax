# Generated by Django 2.2.3 on 2019-11-29 08:39

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('docmanagment', '0021_auto_20191129_0839'),
    ]

    operations = [
        migrations.AlterField(
            model_name='documnet',
            name='created_date',
            field=models.DateField(default=datetime.datetime(2019, 11, 29, 8, 39, 9, 328456), verbose_name='تاریخ ایجاد'),
        ),
    ]