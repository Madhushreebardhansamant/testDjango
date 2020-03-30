# Generated by Django 2.0.2 on 2020-03-30 07:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_userprofileinfo_file'),
    ]

    operations = [
        migrations.RenameField(
            model_name='userprofileinfo',
            old_name='password',
            new_name='email',
        ),
        migrations.RenameField(
            model_name='userprofileinfo',
            old_name='username',
            new_name='location',
        ),
        migrations.RemoveField(
            model_name='userprofileinfo',
            name='file',
        ),
        migrations.AddField(
            model_name='userprofileinfo',
            name='name',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='userprofileinfo',
            name='phone',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='userprofileinfo',
            name='skills',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
