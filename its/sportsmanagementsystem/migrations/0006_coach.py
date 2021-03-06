# Generated by Django 2.0.5 on 2018-09-21 11:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('sportsmanagementsystem', '0005_auto_20180921_1155'),
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
                ('s_name', models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='sportsmanagementsystem.Sport')),
            ],
        ),
    ]
