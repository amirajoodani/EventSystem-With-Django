# Generated by Django 3.2.12 on 2022-07-27 11:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('log', '0026_auto_20220727_1532'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='eventkindofproblem',
            name='start_date',
        ),
        migrations.RemoveField(
            model_name='eventkindofproblem',
            name='start_date2',
        ),
        migrations.RemoveField(
            model_name='historicaleventkindofproblem',
            name='start_date',
        ),
        migrations.RemoveField(
            model_name='historicaleventkindofproblem',
            name='start_date2',
        ),
        migrations.AlterField(
            model_name='minute',
            name='minute',
            field=models.IntegerField(blank=True, max_length=30, null=True),
        ),
    ]
