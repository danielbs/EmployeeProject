# Generated by Django 3.0.4 on 2020-05-16 12:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Department',
            fields=[
                ('dpt_id', models.AutoField(primary_key=True, serialize=False)),
                ('department_name', models.CharField(max_length=250)),
            ],
        ),
        migrations.CreateModel(
            name='Job',
            fields=[
                ('job_id', models.AutoField(primary_key=True, serialize=False)),
                ('job_name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Manager',
            fields=[
                ('mgr_id', models.AutoField(primary_key=True, serialize=False)),
                ('employee_id', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('emp_id', models.AutoField(primary_key=True, serialize=False)),
                ('first_name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=70)),
                ('phone_nr', models.CharField(max_length=25)),
                ('hire_date', models.DateField()),
                ('salary', models.FloatField()),
                ('commission_pct', models.FloatField()),
                ('department_id', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='employees.Department')),
                ('job_id', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='employees.Job')),
                ('manager_id', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='employees.Manager')),
            ],
        ),
    ]