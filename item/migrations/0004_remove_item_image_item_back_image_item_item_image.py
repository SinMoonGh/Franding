# Generated by Django 5.0.3 on 2024-04-30 09:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('item', '0003_remove_category2_detail_cat2_remove_category2_gender_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='item',
            name='image',
        ),
        migrations.AddField(
            model_name='item',
            name='back_image',
            field=models.URLField(null=True),
        ),
        migrations.AddField(
            model_name='item',
            name='item_image',
            field=models.URLField(null=True),
        ),
    ]
