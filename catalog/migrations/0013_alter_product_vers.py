# Generated by Django 5.0b1 on 2023-12-12 21:01

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0012_rename_product_version_prod_product_vers'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='vers',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='catalog.version', verbose_name='версия'),
        ),
    ]
