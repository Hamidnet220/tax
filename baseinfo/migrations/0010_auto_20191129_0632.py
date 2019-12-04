# Generated by Django 2.2.3 on 2019-11-29 06:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('income', '0026_auto_20191119_1826'),
        ('baseinfo', '0009_city_employeer'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Employeer',
            new_name='Employer',
        ),
        migrations.CreateModel(
            name='Contract',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='عنوان قرارداد')),
                ('number', models.CharField(max_length=50, verbose_name='شماره قرارداد')),
                ('date', models.DateField(verbose_name='تاریخ شروع')),
                ('end_date', models.DateField(blank=True, null=True, verbose_name='تاریخ پایان')),
                ('gross_amount', models.DecimalField(decimal_places=2, default=0, max_digits=20, verbose_name='مبلغ اولیه قرارداد')),
                ('adjustment_amount', models.DecimalField(decimal_places=2, default=0, max_digits=20, verbose_name='مبلغ تعدیل')),
                ('final_amount', models.DecimalField(decimal_places=2, default=0, max_digits=20, verbose_name='مبلغ نهایی قرارداد')),
                ('total_payments', models.DecimalField(decimal_places=2, default=0, max_digits=20, verbose_name='مجموع مبالغ دریافتی')),
                ('progress', models.DecimalField(decimal_places=2, default=0, max_digits=10, verbose_name='درصد پیشرفت')),
                ('scan_file', models.FileField(blank=True, upload_to='income/static/contracts', verbose_name='فایل قرارداد')),
                ('description', models.CharField(blank=True, max_length=100, verbose_name='توضیحات')),
                ('employer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='baseinfo.Employer', verbose_name='کارفرما')),
            ],
        ),
    ]