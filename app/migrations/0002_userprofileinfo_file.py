# Generated by Django 2.0.2 on 2020-03-30 01:27

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofileinfo',
            name='file',
            field=models.FileField(default=django.utils.timezone.now, upload_to='media'),
            preserve_default=False,
        ),
    ]
