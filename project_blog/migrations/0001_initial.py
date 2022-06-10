# Generated by Django 3.2.13 on 2022-06-10 17:08

from django.db import migrations, models
import project_blog.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.TextField(max_length=120, verbose_name='عنوان مقاله')),
                ('description', models.TextField(max_length=4000, verbose_name='توضیحات مقاله')),
                ('date', models.DateField(verbose_name='تاریخ')),
                ('slider', models.ImageField(blank=True, null=True, upload_to=project_blog.models.upload_image_path)),
            ],
            options={
                'verbose_name': 'مقالات',
                'verbose_name_plural': 'مقالات',
            },
        ),
    ]
