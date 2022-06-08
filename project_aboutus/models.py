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


class AboutUs(models.Model):
    title = models.TextField(max_length=120, verbose_name='عنوان')
    description = models.CharField(max_length=1000, verbose_name='توضیحات')
    image = models.ImageField(upload_to=upload_image_path, null=True, blank=True)
    slider = models.ImageField(upload_to=upload_image_path, null=True, blank=True)

    class Meta:
        verbose_name = 'درباره ی ما'
        verbose_name_plural = 'درباره ی ما'

    def __str__(self):
        return self.title

