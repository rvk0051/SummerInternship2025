# Generated by Django 5.2.1 on 2025-07-10 14:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('attendance_system', '0003_remove_attendance_is_late_alter_attendance_status'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='attendance',
            options={'ordering': ['-date'], 'verbose_name': 'Attendance', 'verbose_name_plural': 'Attendance'},
        ),
    ]
