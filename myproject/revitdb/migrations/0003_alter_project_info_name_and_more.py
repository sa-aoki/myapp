# Generated by Django 4.1.7 on 2023-07-31 04:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('revitdb', '0002_rename_project_name_project_info_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project_info',
            name='name',
            field=models.CharField(max_length=200, unique=True, verbose_name='プロジェクト名'),
        ),
        migrations.AlterField(
            model_name='project_info',
            name='project_No',
            field=models.CharField(max_length=15, unique=True, verbose_name='設計番号'),
        ),
        migrations.AlterField(
            model_name='project_info',
            name='project_type',
            field=models.CharField(max_length=200, verbose_name='工事種別'),
        ),
    ]