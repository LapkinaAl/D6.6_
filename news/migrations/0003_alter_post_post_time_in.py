# Generated by Django 5.0 on 2023-12-26 05:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0002_alter_post_post_time_in'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='post_time_in',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
