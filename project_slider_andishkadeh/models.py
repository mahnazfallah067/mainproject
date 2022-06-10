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


class SliderAndishkadeh(models.Model):
    title = models.TextField(max_length=120, verbose_name='عنوان')
    image = models.ImageField(upload_to=upload_image_path, null=True, blank=True)

    class Meta:
        verbose_name = 'اسلایدر گروه های علمی و پژوهشی'
        verbose_name_plural = 'اسلایدر گروه های علمی و پژوهشی'

    def __str__(self):
        return self.title


