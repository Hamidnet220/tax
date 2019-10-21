# Generated by Django 2.2.3 on 2019-10-11 08:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('income', '0020_contract_scan_file'),
    ]

    operations = [
        migrations.AddField(
            model_name='contract',
            name='adjustment_amount',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=20, verbose_name='مبلغ تعدیل'),
        ),
        migrations.AlterField(
            model_name='contract',
            name='scan_file',
            field=models.FileField(blank=True, upload_to='income/static/contracts', verbose_name='فایل قرارداد'),
        ),
    ]