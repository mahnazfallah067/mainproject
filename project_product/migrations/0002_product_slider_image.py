# Generated by Django 3.2.13 on 2022-06-02 11:46

from django.db import migrations, models
import project_product.models


class Migration(migrations.Migration):

    dependencies = [
        ('project_product', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='slider_image',
            field=models.ImageField(blank=True, null=True, upload_to=project_product.models.upload_image_path),
        ),
    ]
