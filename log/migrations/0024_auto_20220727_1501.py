# Generated by Django 3.2.12 on 2022-07-27 10:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('log', '0023_eventkindofproblemhistory_historicaleventkindofproblemhistory'),
    ]

    operations = [
        migrations.AddField(
            model_name='eventkindofproblem',
            name='export_to_csv',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='historicaleventkindofproblem',
            name='export_to_csv',
            field=models.BooleanField(default=False),
        ),
    ]
