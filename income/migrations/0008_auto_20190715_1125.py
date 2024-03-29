# Generated by Django 2.2.3 on 2019-07-15 11:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('income', '0007_auto_20190715_1111'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='income',
            name='title',
        ),
        migrations.AddField(
            model_name='income',
            name='contract',
            field=models.ForeignKey(default=1, max_length=150, on_delete=django.db.models.deletion.CASCADE, to='income.Contract', verbose_name='قرارداد'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='contract',
            name='date',
            field=models.DateField(verbose_name='تاریخ'),
        ),
        migrations.AlterField(
            model_name='contract',
            name='description',
            field=models.CharField(blank=True, max_length=100, verbose_name='توضیحات'),
        ),
        migrations.AlterField(
            model_name='contract',
            name='number',
            field=models.CharField(max_length=50, verbose_name='شماره قرارداد'),
        ),
        migrations.AlterField(
            model_name='contract',
            name='title',
            field=models.CharField(max_length=100, verbose_name='عنوان قرارداد'),
        ),
    ]
