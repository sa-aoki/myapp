# Generated by Django 4.1.7 on 2023-07-31 03:46

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Project_info',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('project_No', models.CharField(max_length=15, unique=True, verbose_name='PJ情報 設計番号')),
                ('project_name', models.CharField(max_length=200, unique=True, verbose_name='PJ情報 プロジェクト名')),
                ('project_type', models.CharField(max_length=200, verbose_name='PJ情報 工事種別')),
            ],
        ),
    ]
