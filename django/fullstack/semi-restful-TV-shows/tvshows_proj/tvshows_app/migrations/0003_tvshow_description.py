# Generated by Django 2.2 on 2021-08-05 07:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tvshows_app', '0002_auto_20210805_0525'),
    ]

    operations = [
        migrations.AddField(
            model_name='tvshow',
            name='description',
            field=models.CharField(max_length=255, null=True),
        ),
    ]
