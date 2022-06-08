# Generated by Django 3.2.13 on 2022-06-01 15:20

from django.db import migrations, models
import project_slider.models


class Migration(migrations.Migration):

    dependencies = [
        ('project_slider', '0002_remove_slider_link'),
    ]

    operations = [
        migrations.AddField(
            model_name='slider',
            name='description2',
            field=models.CharField(default='write', max_length=10000, verbose_name='توضیحات'),
        ),
        migrations.AddField(
            model_name='slider',
            name='description3',
            field=models.CharField(default='write', max_length=10000, verbose_name='توضیحات'),
        ),
        migrations.AddField(
            model_name='slider',
            name='image2',
            field=models.ImageField(blank=True, null=True, upload_to=project_slider.models.upload_image_path),
        ),
        migrations.AddField(
            model_name='slider',
            name='image3',
            field=models.ImageField(blank=True, null=True, upload_to=project_slider.models.upload_image_path),
        ),
        migrations.AddField(
            model_name='slider',
            name='title2',
            field=models.TextField(default='write', max_length=200, verbose_name='عنوان'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='slider',
            name='title3',
            field=models.TextField(default='write', max_length=200, verbose_name='عنوان'),
            preserve_default=False,
        ),
    ]