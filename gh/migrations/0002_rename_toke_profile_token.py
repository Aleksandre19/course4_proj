# Generated by Django 3.2.6 on 2023-05-17 13:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gh', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='profile',
            old_name='toke',
            new_name='token',
        ),
    ]
