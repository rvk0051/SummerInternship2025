# Generated by Django 5.2.1 on 2025-07-10 03:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contact_hr', '0002_rename_supportrequest_contacthr'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contacthr',
            name='status',
            field=models.CharField(choices=[('Pending', 'Pending'), ('Resolved', 'Resolved')], default='Pending', max_length=25),
        ),
    ]
