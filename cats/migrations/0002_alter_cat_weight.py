# Generated by Django 3.2.3 on 2021-07-29 23:57

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cats', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cat',
            name='weight',
            field=models.FloatField(validators=[django.core.validators.MinValueValidator(0.0, 'Weight must be greater than 0.')]),
        ),
    ]