# Generated by Django 2.1.7 on 2019-10-10 06:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('income', '0017_contract_progress'),
    ]

    operations = [
        migrations.AddField(
            model_name='income',
            name='title',
            field=models.CharField(blank=True, max_length=100, verbose_name='عنوان پرداخت'),
        ),
    ]
