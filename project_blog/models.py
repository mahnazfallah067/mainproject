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


class Blog(models.Model):
    title = models.TextField(max_length=120, verbose_name='عنوان مقاله یا نشست')
    description = models.TextField(max_length=4000, verbose_name='توضیحات')
    date = models.DateField(verbose_name='تاریخ')
    image = models.ImageField(upload_to=upload_image_path, null=True, blank=True)

    class Meta:
        verbose_name = 'مقالات و نشست ها'
        verbose_name_plural = 'مقالات و نشست ها'

    def __str__(self):
        return self.title

