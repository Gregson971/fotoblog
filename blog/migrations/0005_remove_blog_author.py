# Generated by Django 4.2.7 on 2023-11-20 22:26

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("blog", "0004_auto_20231120_2215"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="blog",
            name="author",
        ),
    ]
