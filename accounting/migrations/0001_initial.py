# Generated by Django 2.2.3 on 2019-11-26 03:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='HesabKol',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='HesabMoein',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('hesab_kol', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accounting.HesabKol')),
            ],
        ),
        migrations.CreateModel(
            name='HesabTafzili',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('hesb_moien', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accounting.HesabMoein')),
            ],
        ),
        migrations.CreateModel(
            name='Sanad',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('year', models.IntegerField()),
                ('month', models.IntegerField()),
                ('day', models.IntegerField()),
                ('bedehkar', models.DecimalField(decimal_places=2, default=0, max_digits=20)),
                ('bestankar', models.DecimalField(decimal_places=2, default=0, max_digits=20)),
                ('hesab_tafzili', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accounting.HesabTafzili')),
            ],
        ),
    ]
