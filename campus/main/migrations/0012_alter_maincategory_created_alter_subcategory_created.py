# Generated by Django 4.0.4 on 2022-09-29 02:05

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0011_alter_maincategory_created_alter_subcategory_created'),
    ]

    operations = [
        migrations.AlterField(
            model_name='maincategory',
            name='created',
            field=models.DateTimeField(default=datetime.datetime(2022, 9, 29, 2, 5, 34, 81717, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='subcategory',
            name='created',
            field=models.DateTimeField(default=datetime.datetime(2022, 9, 29, 2, 5, 34, 81717, tzinfo=utc)),
        ),
    ]