# Generated by Django 2.2 on 2021-08-07 19:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('loginApp', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='pasword',
            new_name='password',
        ),
    ]
