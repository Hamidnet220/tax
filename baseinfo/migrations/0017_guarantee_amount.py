# Generated by Django 2.1.7 on 2019-12-06 08:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('baseinfo', '0016_auto_20191206_0806'),
    ]

    operations = [
        migrations.AddField(
            model_name='guarantee',
            name='amount',
            field=models.DecimalField(decimal_places=0, default=0, max_digits=20, verbose_name='مبلغ ضمانت نامه'),
        ),
    ]