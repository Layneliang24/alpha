# Generated by Django 4.0.4 on 2022-09-22 06:56

import datetime
from django.db import migrations, models
import django.db.models.deletion
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='category',
            field=models.ForeignKey(default='1', on_delete=django.db.models.deletion.CASCADE, related_name='subcategory', to='main.subcategory'),
        ),
        migrations.AlterField(
            model_name='maincategory',
            name='created',
            field=models.DateTimeField(default=datetime.datetime(2022, 9, 22, 6, 56, 20, 322181, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='subcategory',
            name='created',
            field=models.DateTimeField(default=datetime.datetime(2022, 9, 22, 6, 56, 20, 323179, tzinfo=utc)),
        ),
    ]