# Generated by Django 2.0.5 on 2018-09-21 11:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sportsmanagementsystem', '0004_auto_20180921_1148'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='coach',
            name='s_name',
        ),
        migrations.DeleteModel(
            name='Coach',
        ),
    ]
