# Generated by Django 2.2.2 on 2019-06-27 00:25

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='portList',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('serviceName', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='internalapp',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('appGrpNm', models.CharField(max_length=100, verbose_name='Application Group Name')),
                ('servGrpNm', models.CharField(max_length=100, null=True, verbose_name='Service Group Name')),
                ('perimeter', models.CharField(choices=[('ALL', 'All'), ('ECN', 'ECN'), ('GIZ', 'GIZ')], default='All', max_length=10, verbose_name='Perimeter')),
                ('groupInd', models.IntegerField(verbose_name='Group Index')),
                ('appGrpFunc', models.CharField(max_length=100, null=True, verbose_name='Application Group Function')),
                ('paloApp', models.CharField(max_length=1000, null=True, verbose_name='PaloAlto Application')),
                ('services', models.CharField(max_length=1000, null=True, verbose_name='Services')),
                ('plServConfig', models.CharField(max_length=1000, null=True, verbose_name='PaloAlto Service Config')),
                ('plAppConfig', models.CharField(max_length=1000, null=True, verbose_name='PaloAlto Application Config')),
                ('comment', models.CharField(max_length=1000, null=True, verbose_name='Comments')),
                ('createdDt', models.DateField(default=datetime.date.today, verbose_name='Creation Date')),
                ('ports', models.ManyToManyField(blank=True, to='tryout.portList')),
            ],
        ),
    ]
