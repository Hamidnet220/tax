# Generated by Django 2.2.3 on 2019-11-28 05:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('baseinfo', '0002_auto_20191127_0544'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contract',
            name='description',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='توضیحات'),
        ),
    ]
