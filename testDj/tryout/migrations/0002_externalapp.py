# Generated by Django 2.2.2 on 2019-07-12 16:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tryout', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='externalapp',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('appGrpNm', models.CharField(max_length=100, verbose_name='Application Group Name')),
                ('servGrpNm', models.CharField(max_length=100, null=True, verbose_name='Service Group Name')),
                ('ports', models.ManyToManyField(blank=True, to='tryout.portList')),
            ],
        ),
    ]
