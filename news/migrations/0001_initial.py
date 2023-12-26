# Generated by Django 5.0 on 2023-12-26 02:33

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('post_name', models.CharField(max_length=255)),
                ('post_text', models.CharField(max_length=10000)),
                ('post_time_in', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
