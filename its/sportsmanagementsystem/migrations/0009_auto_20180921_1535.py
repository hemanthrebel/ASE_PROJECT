# Generated by Django 2.0.5 on 2018-09-21 15:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sportsmanagementsystem', '0008_auto_20180921_1531'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='coach',
            name='s_name',
        ),
        migrations.DeleteModel(
            name='Complaint',
        ),
        migrations.RemoveField(
            model_name='notification',
            name='sport_id',
        ),
        migrations.RemoveField(
            model_name='performance',
            name='sport_id',
        ),
        migrations.RemoveField(
            model_name='performance',
            name='student_id',
        ),
        migrations.RemoveField(
            model_name='schedule',
            name='s_name',
        ),
        migrations.RemoveField(
            model_name='tournament',
            name='s_name',
        ),
        migrations.DeleteModel(
            name='Coach',
        ),
        migrations.DeleteModel(
            name='Notification',
        ),
        migrations.DeleteModel(
            name='Performance',
        ),
        migrations.DeleteModel(
            name='Schedule',
        ),
        migrations.DeleteModel(
            name='Tournament',
        ),
    ]
