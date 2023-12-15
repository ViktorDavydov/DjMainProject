# Generated by Django 5.0b1 on 2023-12-12 18:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0010_alter_version_options'),
    ]

    operations = [
        migrations.AlterField(
            model_name='version',
            name='is_active',
            field=models.BooleanField(default=False, verbose_name='активна'),
        ),
        migrations.AlterField(
            model_name='version',
            name='version_number',
            field=models.IntegerField(verbose_name='версия'),
        ),
    ]