# Generated by Django 3.2.13 on 2022-06-07 12:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('project_product', '0010_product_slug'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='slug',
        ),
    ]
