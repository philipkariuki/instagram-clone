# Generated by Django 2.2.3 on 2019-07-28 19:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('instaclone', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='last_login',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
