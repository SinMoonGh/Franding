# Generated by Django 5.0.3 on 2024-04-30 16:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('payment', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='delivery',
            name='receiver_email',
            field=models.EmailField(max_length=254, null=True),
        ),
    ]
