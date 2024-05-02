# Generated by Django 5.0.3 on 2024-05-02 15:46

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mypage', '0003_useraddinfo_user_name'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.RemoveField(
            model_name='useraddinfo',
            name='user_name',
        ),
        migrations.AddField(
            model_name='useraddinfo',
            name='detailAddress',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='useraddinfo',
            name='extraAddress',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='useraddinfo',
            name='postcode',
            field=models.CharField(max_length=6, null=True),
        ),
        migrations.AlterField(
            model_name='useraddinfo',
            name='address',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='useraddinfo',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
