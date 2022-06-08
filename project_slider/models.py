from django.db import models
import os

# Create your models here.


def get_filename_ext(filepath):
    base_name = os.path.basename(filepath)
    ext = os.path.splitext(base_name)
    return ext


def upload_image_path(instance, filename):
    ext = get_filename_ext(filename)
    finalname = f"{instance.id} - {instance.title}{ext}"
    return f"{finalname}"


class Slider(models.Model):
    title = models.TextField(max_length=200, verbose_name='عنوان')
    title2 = models.TextField(max_length=200, verbose_name='عنوان')
    title3 = models.TextField(max_length=200, verbose_name='عنوان')
    description = models.CharField(max_length=10000, verbose_name='توضیحات')
    description2 = models.CharField(max_length=10000, verbose_name='توضیحات', default='write')
    description3 = models.CharField(max_length=10000, verbose_name='توضیحات', default='write')

    image = models.ImageField(upload_to=upload_image_path, null=True, blank=True)
    image2 = models.ImageField(upload_to=upload_image_path, null=True, blank=True)
    image3 = models.ImageField(upload_to=upload_image_path, null=True, blank=True)

    class Meta:
        verbose_name = 'اسلایدر',
        verbose_name_plural = 'اسلایدر'

    def __str__(self):
        return self.title



