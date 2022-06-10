# Generated by Django 3.2.13 on 2022-06-10 10:23

from django.db import migrations, models
import project_researche.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ReSearche',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=120, verbose_name='عنوان پژوهش')),
                ('description', models.TextField(max_length=2000, verbose_name='توضیحات پژوهش')),
                ('researcher_name', models.CharField(max_length=120, verbose_name='نام پژوهشگر')),
                ('date', models.DateTimeField(verbose_name='تاریخ')),
                ('slider', models.ImageField(blank=True, null=True, upload_to=project_researche.models.upload_image_path)),
            ],
            options={
                'verbose_name': 'پژوهش های مرکز',
                'verbose_name_plural': 'پژوهش های مرکز',
            },
        ),
    ]