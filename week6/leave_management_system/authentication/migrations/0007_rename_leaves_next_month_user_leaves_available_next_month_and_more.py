# Generated by Django 5.2.1 on 2025-06-27 08:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0006_user_leaves_next_month_user_leaves_this_month'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='leaves_next_month',
            new_name='leaves_available_next_month',
        ),
        migrations.RenameField(
            model_name='user',
            old_name='leaves_this_month',
            new_name='leaves_available_this_month',
        ),
    ]
