# Generated by Django 4.2.4 on 2023-08-02 10:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('revitdb', '0008_document'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='document',
            name='description',
        ),
    ]
