# Generated by Django 3.2.12 on 2022-07-18 13:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('log', '0016_auto_20220718_1740'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mounth',
            name='mounth',
            field=models.CharField(blank=True, max_length=300, null=True),
        ),
    ]