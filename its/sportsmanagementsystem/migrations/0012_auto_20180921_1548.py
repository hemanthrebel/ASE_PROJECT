# Generated by Django 2.0.5 on 2018-09-21 15:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('sportsmanagementsystem', '0011_auto_20180921_1547'),
    ]

    operations = [
        migrations.CreateModel(
            name='Coach',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('coach_id', models.CharField(max_length=12)),
                ('c_name', models.CharField(max_length=42)),
                ('coach_type', models.CharField(max_length=10)),
                ('experience', models.IntegerField()),
                ('contact', models.CharField(max_length=200)),
                ('password', models.CharField(max_length=50, verbose_name='password')),
            ],
        ),
        migrations.CreateModel(
            name='Complaint',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('student_id', models.CharField(max_length=12)),
                ('about', models.TextField(max_length=42)),
                ('DateTimeField', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Notification',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Notification_id', models.IntegerField()),
                ('sender', models.CharField(max_length=10)),
                ('receiver', models.CharField(max_length=200)),
                ('message', models.TextField()),
                ('send_date', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='Performance',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('role', models.CharField(max_length=10)),
                ('performance', models.CharField(max_length=200)),
                ('date', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='Player',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('student_id', models.CharField(max_length=12)),
                ('p_name', models.CharField(max_length=42)),
                ('email_id', models.EmailField(max_length=75)),
                ('contact', models.CharField(max_length=10)),
                ('sport_id', models.CharField(max_length=200)),
                ('password', models.CharField(max_length=50, verbose_name='password')),
                ('joined_date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Schedule',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Tournament_name', models.CharField(max_length=12)),
                ('team_1', models.CharField(max_length=10)),
                ('team_2', models.CharField(max_length=200)),
                ('date', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='Sport',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sport_id', models.CharField(max_length=12)),
                ('s_name', models.CharField(max_length=42)),
                ('kit', models.CharField(max_length=75)),
                ('catogery', models.CharField(max_length=10)),
                ('no_of_players_per_team', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Tournament',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Tournament_id', models.CharField(max_length=12)),
                ('team_1', models.CharField(max_length=10)),
                ('team_2', models.CharField(max_length=200)),
                ('start_date', models.DateTimeField()),
                ('end_date', models.DateTimeField()),
                ('result', models.CharField(max_length=50)),
                ('s_name', models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='sportsmanagementsystem.Sport')),
            ],
        ),
        migrations.AddField(
            model_name='schedule',
            name='s_name',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='sportsmanagementsystem.Sport'),
        ),
        migrations.AddField(
            model_name='performance',
            name='sport_id',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='sportsmanagementsystem.Sport'),
        ),
        migrations.AddField(
            model_name='performance',
            name='student_id',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='sportsmanagementsystem.Player'),
        ),
        migrations.AddField(
            model_name='notification',
            name='sport_id',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='sportsmanagementsystem.Sport'),
        ),
        migrations.AddField(
            model_name='coach',
            name='s_name',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='sportsmanagementsystem.Sport'),
        ),
    ]
