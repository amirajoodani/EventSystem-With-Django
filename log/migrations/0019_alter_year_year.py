# Generated by Django 3.2.12 on 2022-07-24 15:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('log', '0018_alter_year_year'),
    ]

    operations = [
        migrations.AlterField(
            model_name='year',
            name='year',
            field=models.CharField(blank=True, max_length=300, null=True),
        ),
    ]
