# Generated by Django 2.2.3 on 2019-10-11 09:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('income', '0021_auto_20191011_0844'),
    ]

    operations = [
        migrations.AddField(
            model_name='contract',
            name='total_payments',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=20, verbose_name='مجموع مبالغ دریافتی'),
        ),
    ]