from django.db import models

# Create your models here.


class ContactUs(models.Model):
    family = models.CharField(max_length=100, verbose_name='نام و نام خانوادگی', null=True, blank=True)
    email = models.EmailField(max_length=100, verbose_name='ایمیل')
    text = models.TextField(max_length=1000, verbose_name='پیام')
    number = models.IntegerField(max_length=11, verbose_name='شماره')

    class Meta:
        verbose_name = 'تماس با ما'
        verbose_name_plural = 'تماس با ما'

    def __str__(self):
        return self.family