# Generated by Django 4.2 on 2023-04-27 09:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_alter_user_age'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='introduction',
            field=models.TextField(blank=True, max_length=200, verbose_name='자기소개'),
        ),
    ]
