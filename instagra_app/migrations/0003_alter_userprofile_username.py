# Generated by Django 4.0.5 on 2022-06-03 18:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('instagra_app', '0002_userprofile_username'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='username',
            field=models.CharField(max_length=30),
        ),
    ]
