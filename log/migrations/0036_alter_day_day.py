# Generated by Django 3.2.12 on 2022-07-31 11:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('log', '0035_auto_20220730_1251'),
    ]

    operations = [
        migrations.AlterField(
            model_name='day',
            name='day',
            field=models.IntegerField(blank=True, max_length=30, null=True),
        ),
    ]
