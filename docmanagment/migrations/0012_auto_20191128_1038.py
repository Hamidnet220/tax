# Generated by Django 2.2.3 on 2019-11-28 10:38

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('docmanagment', '0011_auto_20191128_1037'),
    ]

    operations = [
        migrations.AlterField(
            model_name='documnet',
            name='created_date',
            field=models.DateField(default=datetime.datetime(2019, 11, 28, 10, 38, 26, 13265, tzinfo=utc), verbose_name='تاریخ ایجاد'),
        ),
    ]
