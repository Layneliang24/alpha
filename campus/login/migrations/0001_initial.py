# Generated by Django 4.0.4 on 2022-09-22 04:48

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('gender', models.CharField(choices=[('male', '男'), ('female', '女')], default='女', max_length=32)),
                ('nickname', models.CharField(blank=True, max_length=191)),
                ('phone', models.CharField(blank=True, max_length=20)),
                ('portrait', models.ImageField(blank=True, upload_to='portrait/%Y%m%d/')),
                ('resume', models.TextField(blank=True, max_length=500)),
                ('has_confirmed', models.BooleanField(default=False)),
                ('c_time', models.DateTimeField(auto_now_add=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='profile', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'user',
                'ordering': ['-c_time'],
            },
        ),
        migrations.CreateModel(
            name='ConfirmString',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=256)),
                ('c_time', models.DateTimeField(auto_now_add=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'confirm code',
                'verbose_name_plural': 'confirm code',
                'ordering': ['-c_time'],
            },
        ),
    ]