# Generated by Django 3.2.12 on 2022-07-18 09:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('log', '0012_historicaleventkindofproblem'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='eventkindofproblem',
            name='Status_Of_problem',
        ),
        migrations.RemoveField(
            model_name='eventkindofproblem',
            name='reson',
        ),
        migrations.RemoveField(
            model_name='eventkindofproblem',
            name='status',
        ),
        migrations.RemoveField(
            model_name='historicaleventkindofproblem',
            name='Status_Of_problem',
        ),
        migrations.RemoveField(
            model_name='historicaleventkindofproblem',
            name='reson',
        ),
        migrations.RemoveField(
            model_name='historicaleventkindofproblem',
            name='status',
        ),
    ]
