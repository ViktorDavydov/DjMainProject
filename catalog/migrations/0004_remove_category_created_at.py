# Generated by Django 5.0b1 on 2023-11-20 19:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0003_category_created_at'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='category',
            name='created_at',
        ),
    ]
