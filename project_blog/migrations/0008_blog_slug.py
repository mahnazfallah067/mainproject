# Generated by Django 3.2.13 on 2022-06-14 12:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('project_blog', '0007_alter_comment_body'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='slug',
            field=models.SlugField(default='slug'),
        ),
    ]
