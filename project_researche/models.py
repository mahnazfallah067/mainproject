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


class ReSearche(models.Model):
    title = models.CharField(max_length=120, verbose_name='عنوان پژوهش')
    description = models.TextField(max_length=2000, verbose_name='توضیحات پژوهش')
    researcher_name = models.CharField(max_length=120, verbose_name='نام پژوهشگر')
    date = models.DateTimeField(verbose_name='تاریخ')
    image = models.ImageField(upload_to=upload_image_path, null=True, blank=False, verbose_name='عکس')
    slider = models.ImageField(upload_to=upload_image_path, null=True, blank=True)

    class Meta:
        verbose_name = 'پژوهش های مرکز'
        verbose_name_plural = 'پژوهش های مرکز'

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return f"/research_detail/{self.id}"
