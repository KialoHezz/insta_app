# Generated by Django 4.0.5 on 2022-06-04 09:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('instagra_app', '0004_alter_userprofile_username'),
    ]

    operations = [
        migrations.AlterField(
            model_name='imagein',
            name='likes',
            field=models.IntegerField(blank=True),
        ),
    ]
