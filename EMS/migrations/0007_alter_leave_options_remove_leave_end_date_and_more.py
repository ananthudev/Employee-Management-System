# Generated by Django 5.0.6 on 2024-06-27 19:05

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ems', '0006_remove_project_employee_project_employees'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='leave',
            options={'verbose_name_plural': 'Leaves'},
        ),
        migrations.RemoveField(
            model_name='leave',
            name='end_date',
        ),
        migrations.RemoveField(
            model_name='leave',
            name='start_date',
        ),
        migrations.AddField(
            model_name='leave',
            name='apply_date',
            field=models.DateField(auto_now_add=True, null=True),
        ),
        migrations.AddField(
            model_name='leave',
            name='from_date',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='leave',
            name='leave_type',
            field=models.CharField(choices=[('casual', 'Casual'), ('sick', 'Sick'), ('personal', 'Personal'), ('vacation', 'Vacation')], max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='leave',
            name='to_date',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='leave',
            name='employee',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='ems.employee'),
        ),
        migrations.AlterField(
            model_name='leave',
            name='reason',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='leave',
            name='status',
            field=models.CharField(choices=[('pending', 'Pending'), ('approved', 'Approved'), ('rejected', 'Rejected')], default='pending', max_length=20, null=True),
        ),
    ]