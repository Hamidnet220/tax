# Generated by Django 2.2.3 on 2019-11-26 03:22

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('docmanagment', '0003_auto_20191126_0318'),
    ]

    operations = [
        migrations.AlterField(
            model_name='documnet',
            name='created_date',
            field=models.DateField(default=datetime.datetime(2019, 11, 26, 3, 22, 6, 866363, tzinfo=utc), verbose_name='تاریخ ایجاد'),
        ),
    ]