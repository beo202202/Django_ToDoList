# Generated by Django 4.2 on 2023-04-29 04:32

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('email', models.EmailField(max_length=255, unique=True, verbose_name='이메일')),
                ('name', models.CharField(max_length=50, verbose_name='이름')),
                ('gender', models.CharField(choices=[('M', 'Male'), ('F', 'Female'), ('O', 'Other')], max_length=1, verbose_name='성별')),
                ('age', models.PositiveIntegerField(verbose_name='나이')),
                ('introduction', models.TextField(blank=True, max_length=200, verbose_name='자기 소개')),
                ('is_active', models.BooleanField(default=True, verbose_name='활성화 여부')),
                ('is_admin', models.BooleanField(default=False, verbose_name='관리자 여부')),
            ],
            options={
                'db_table': 'user',
            },
        ),
    ]
