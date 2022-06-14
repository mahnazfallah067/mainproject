from django.contrib.auth.models import User
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
    post = models.ForeignKey(User, on_delete=models.CASCADE, related_name='posts')
    title = models.TextField(max_length=120, verbose_name='عنوان مقاله یا نشست')
    description = models.TextField(max_length=4000, verbose_name='توضیحات')
    description2 = models.TextField(max_length=4000, verbose_name='ادامه توضیحات')
    purpose = models.TextField(max_length=200, verbose_name='اهداف نشست یا مقاله')
    date = models.DateField(verbose_name='تاریخ')
    image = models.ImageField(upload_to=upload_image_path, null=True, blank=True)
    slug = models.SlugField(max_length=50, default='slug')

    class Meta:
        verbose_name = 'مقالات و نشست ها'
        verbose_name_plural = 'مقالات و نشست ها'

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return f"/blog-detail/{self.id}/{self.slug}"


class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='ucomments')
    post = models.ForeignKey(Blog, on_delete=models.CASCADE, related_name='pcomments')
    reply = models.ForeignKey('Comment', on_delete=models.CASCADE, related_name='rcomments', blank=True, null=True)
    body = models.TextField(max_length=200, default='default', verbose_name='متن ')
    email = models.EmailField(default='email', verbose_name='ایمیل')
    name = models.CharField(max_length=10, verbose_name='نام شما', default='name')

    class Meta:
        verbose_name = 'دیدگاه ها'
        verbose_name_plural = 'دیدگاه ها'

    def __str__(self):
         return f"{self.user}-{self.body[:30]}"

