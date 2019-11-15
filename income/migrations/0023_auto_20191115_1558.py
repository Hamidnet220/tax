# Generated by Django 2.2.3 on 2019-11-15 15:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('income', '0022_contract_total_payments'),
    ]

    operations = [
        migrations.AlterField(
            model_name='income',
            name='VAT_included',
            field=models.BooleanField(choices=[(True, 'مشمول'), (False, 'معاف')], default=True, verbose_name='مالیات بر ارزش افزوده '),
        ),
        migrations.AlterField(
            model_name='income',
            name='day',
            field=models.IntegerField(choices=[(1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5'), (6, '6'), (7, '7'), (8, '8'), (9, '9'), (10, '10'), (11, '11'), (12, '12'), (13, '13'), (14, '14'), (15, '15'), (16, '16'), (17, '17'), (18, '18'), (19, '19'), (20, '20'), (21, '21'), (22, '22'), (23, '23'), (24, '24'), (25, '25'), (26, '26'), (27, '27'), (28, '28'), (29, '29'), (30, '30'), (31, '31')], verbose_name='روز'),
        ),
        migrations.AlterField(
            model_name='income',
            name='month',
            field=models.IntegerField(choices=[(1, 'فروردین'), (2, 'اردیبشت'), (3, 'خرداد'), (3, 'تیر'), (5, 'مرداد'), (6, 'شهریور'), (7, 'مهر'), (8, 'آبان'), (9, 'آذر'), (10, 'دی'), (11, 'بهمن'), (12, 'اسفند')], verbose_name='ماه'),
        ),
        migrations.AlterField(
            model_name='income',
            name='tax_included',
            field=models.BooleanField(choices=[(True, 'مشمول'), (False, 'معاف')], default=True, verbose_name='وضعیت مالیات تکلیفی'),
        ),
        migrations.AlterField(
            model_name='income',
            name='year',
            field=models.IntegerField(choices=[(1396, '1396'), (1397, '1397'), (1398, '1398'), (1399, '1399'), (1400, '1400')], verbose_name='سال'),
        ),
        migrations.CreateModel(
            name='Buy',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('economic_id', models.CharField(max_length=11, verbose_name='شماره اقتصادی')),
                ('national_code', models.CharField(max_length=11, verbose_name='شماره/شناسه ملی')),
                ('title', models.CharField(blank=True, max_length=100, verbose_name='عنوان خرید')),
                ('year', models.IntegerField(choices=[(1396, '1396'), (1397, '1397'), (1398, '1398'), (1399, '1399'), (1400, '1400')], verbose_name='سال')),
                ('month', models.IntegerField(choices=[(1, 'فروردین'), (2, 'اردیبشت'), (3, 'خرداد'), (3, 'تیر'), (5, 'مرداد'), (6, 'شهریور'), (7, 'مهر'), (8, 'آبان'), (9, 'آذر'), (10, 'دی'), (11, 'بهمن'), (12, 'اسفند')], verbose_name='ماه')),
                ('day', models.IntegerField(choices=[(1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5'), (6, '6'), (7, '7'), (8, '8'), (9, '9'), (10, '10'), (11, '11'), (12, '12'), (13, '13'), (14, '14'), (15, '15'), (16, '16'), (17, '17'), (18, '18'), (19, '19'), (20, '20'), (21, '21'), (22, '22'), (23, '23'), (24, '24'), (25, '25'), (26, '26'), (27, '27'), (28, '28'), (29, '29'), (30, '30'), (31, '31')], verbose_name='روز')),
                ('doc_number', models.CharField(max_length=30, verbose_name='شماره فاکتور')),
                ('gross_amount', models.DecimalField(decimal_places=2, max_digits=20, verbose_name='مبلغ ناخالص')),
                ('VAT_included', models.BooleanField(choices=[(True, 'مشمول'), (False, 'معاف')], default=True, verbose_name='مالیات بر ارزش افزوده ')),
                ('VAT_amount', models.DecimalField(decimal_places=2, max_digits=20, verbose_name='مبلغ ارزش افزوده')),
                ('pay_amount', models.DecimalField(decimal_places=2, default=0, max_digits=20, verbose_name='مبلغ پرداختی')),
                ('phone_number', models.CharField(max_length=11, verbose_name='شماره تلفن')),
                ('address', models.TextField(verbose_name='آدرس')),
                ('description', models.CharField(blank=True, max_length=100, null=True)),
                ('city_name', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='income.City', verbose_name='شهر')),
                ('contract', models.ForeignKey(max_length=150, on_delete=django.db.models.deletion.CASCADE, to='income.Contract', verbose_name='قرارداد')),
                ('employeer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='income.Employeer', verbose_name='کارفرما')),
            ],
            options={
                'ordering': ['year', 'month', 'day'],
            },
        ),
    ]
