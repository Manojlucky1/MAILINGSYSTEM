# Generated by Django 5.1.2 on 2025-01-22 08:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0005_mails_created_at'),
    ]

    operations = [
        migrations.RenameField(
            model_name='mails',
            old_name='created_at',
            new_name='sent_at',
        ),
    ]
