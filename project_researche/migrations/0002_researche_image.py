# Generated by Django 3.2.13 on 2022-06-10 10:26

from django.db import migrations, models
import project_researche.models


class Migration(migrations.Migration):

    dependencies = [
        ('project_researche', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='researche',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to=project_researche.models.upload_image_path),
        ),
    ]
