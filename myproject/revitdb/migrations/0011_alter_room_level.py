# Generated by Django 4.2.4 on 2023-08-03 04:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('revitdb', '0010_level'),
    ]

    operations = [
        migrations.AlterField(
            model_name='room',
            name='level',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='revitdb.level', verbose_name='レベル'),
        ),
    ]
