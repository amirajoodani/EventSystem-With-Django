# Generated by Django 3.2.12 on 2022-08-10 09:57

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('log', '0039_auto_20220731_1738'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='eventkindofproblem',
            name='day_of_end2',
        ),
        migrations.RemoveField(
            model_name='eventkindofproblem',
            name='day_of_start2',
        ),
        migrations.RemoveField(
            model_name='eventkindofproblem',
            name='hour_of_end2',
        ),
        migrations.RemoveField(
            model_name='eventkindofproblem',
            name='hour_of_start2',
        ),
        migrations.RemoveField(
            model_name='eventkindofproblem',
            name='minute_of_end2',
        ),
        migrations.RemoveField(
            model_name='eventkindofproblem',
            name='minute_of_start2',
        ),
        migrations.RemoveField(
            model_name='eventkindofproblem',
            name='mounth_of_end2',
        ),
        migrations.RemoveField(
            model_name='eventkindofproblem',
            name='mounth_of_start2',
        ),
        migrations.RemoveField(
            model_name='eventkindofproblem',
            name='year_of_end2',
        ),
        migrations.RemoveField(
            model_name='eventkindofproblem',
            name='year_of_start2',
        ),
        migrations.RemoveField(
            model_name='historicaleventkindofproblem',
            name='day_of_end2',
        ),
        migrations.RemoveField(
            model_name='historicaleventkindofproblem',
            name='day_of_start2',
        ),
        migrations.RemoveField(
            model_name='historicaleventkindofproblem',
            name='hour_of_end2',
        ),
        migrations.RemoveField(
            model_name='historicaleventkindofproblem',
            name='hour_of_start2',
        ),
        migrations.RemoveField(
            model_name='historicaleventkindofproblem',
            name='minute_of_end2',
        ),
        migrations.RemoveField(
            model_name='historicaleventkindofproblem',
            name='minute_of_start2',
        ),
        migrations.RemoveField(
            model_name='historicaleventkindofproblem',
            name='mounth_of_end2',
        ),
        migrations.RemoveField(
            model_name='historicaleventkindofproblem',
            name='mounth_of_start2',
        ),
        migrations.RemoveField(
            model_name='historicaleventkindofproblem',
            name='year_of_end2',
        ),
        migrations.RemoveField(
            model_name='historicaleventkindofproblem',
            name='year_of_start2',
        ),
        migrations.AlterField(
            model_name='eventkindofproblem',
            name='day_of_end',
            field=models.IntegerField(blank=True, null=True, validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(31)]),
        ),
        migrations.AlterField(
            model_name='eventkindofproblem',
            name='day_of_start',
            field=models.IntegerField(null=True, validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(31)]),
        ),
        migrations.AlterField(
            model_name='eventkindofproblem',
            name='hour_of_end',
            field=models.IntegerField(blank=True, null=True, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(24)]),
        ),
        migrations.AlterField(
            model_name='eventkindofproblem',
            name='hour_of_start',
            field=models.IntegerField(null=True, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(24)]),
        ),
        migrations.AlterField(
            model_name='eventkindofproblem',
            name='minute_of_end',
            field=models.IntegerField(blank=True, null=True, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(24)]),
        ),
        migrations.AlterField(
            model_name='eventkindofproblem',
            name='minute_of_start',
            field=models.IntegerField(null=True, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(59)]),
        ),
        migrations.AlterField(
            model_name='eventkindofproblem',
            name='mounth_of_end',
            field=models.IntegerField(blank=True, null=True, validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(12)]),
        ),
        migrations.AlterField(
            model_name='eventkindofproblem',
            name='mounth_of_start',
            field=models.IntegerField(null=True, validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(12)]),
        ),
        migrations.AlterField(
            model_name='eventkindofproblem',
            name='year_of_end',
            field=models.IntegerField(blank=True, null=True, validators=[django.core.validators.MinValueValidator(1401), django.core.validators.MaxValueValidator(1500)]),
        ),
        migrations.AlterField(
            model_name='eventkindofproblem',
            name='year_of_start',
            field=models.IntegerField(null=True, validators=[django.core.validators.MinValueValidator(1401), django.core.validators.MaxValueValidator(1500)]),
        ),
        migrations.AlterField(
            model_name='historicaleventkindofproblem',
            name='day_of_end',
            field=models.IntegerField(blank=True, null=True, validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(31)]),
        ),
        migrations.AlterField(
            model_name='historicaleventkindofproblem',
            name='day_of_start',
            field=models.IntegerField(null=True, validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(31)]),
        ),
        migrations.AlterField(
            model_name='historicaleventkindofproblem',
            name='hour_of_end',
            field=models.IntegerField(blank=True, null=True, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(24)]),
        ),
        migrations.AlterField(
            model_name='historicaleventkindofproblem',
            name='hour_of_start',
            field=models.IntegerField(null=True, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(24)]),
        ),
        migrations.AlterField(
            model_name='historicaleventkindofproblem',
            name='minute_of_end',
            field=models.IntegerField(blank=True, null=True, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(24)]),
        ),
        migrations.AlterField(
            model_name='historicaleventkindofproblem',
            name='minute_of_start',
            field=models.IntegerField(null=True, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(59)]),
        ),
        migrations.AlterField(
            model_name='historicaleventkindofproblem',
            name='mounth_of_end',
            field=models.IntegerField(blank=True, null=True, validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(12)]),
        ),
        migrations.AlterField(
            model_name='historicaleventkindofproblem',
            name='mounth_of_start',
            field=models.IntegerField(null=True, validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(12)]),
        ),
        migrations.AlterField(
            model_name='historicaleventkindofproblem',
            name='year_of_end',
            field=models.IntegerField(blank=True, null=True, validators=[django.core.validators.MinValueValidator(1401), django.core.validators.MaxValueValidator(1500)]),
        ),
        migrations.AlterField(
            model_name='historicaleventkindofproblem',
            name='year_of_start',
            field=models.IntegerField(null=True, validators=[django.core.validators.MinValueValidator(1401), django.core.validators.MaxValueValidator(1500)]),
        ),
    ]
