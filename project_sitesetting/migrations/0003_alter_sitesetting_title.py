# Generated by Django 3.2.13 on 2022-06-09 15:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('project_sitesetting', '0002_remove_sitesetting_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sitesetting',
            name='title',
            field=models.TextField(max_length=100, verbose_name='عنوان'),
        ),
    ]
