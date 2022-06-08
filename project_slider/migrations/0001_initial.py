# Generated by Django 3.2.13 on 2022-06-01 13:59

from django.db import migrations, models
import project_slider.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Slider',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.TextField(max_length=200, verbose_name='عنوان')),
                ('description', models.CharField(max_length=10000, verbose_name='توضیحات')),
                ('link', models.URLField(max_length=120, verbose_name='لینک')),
                ('image', models.ImageField(blank=True, null=True, upload_to=project_slider.models.upload_image_path)),
            ],
        ),
    ]
