# Generated by Django 2.2.3 on 2019-11-30 04:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('income', '0028_auto_20191129_0835'),
    ]

    operations = [
        migrations.RenameField(
            model_name='buy',
            old_name='employeer',
            new_name='employer',
        ),
        migrations.RenameField(
            model_name='income',
            old_name='employeer',
            new_name='employer',
        ),
    ]
