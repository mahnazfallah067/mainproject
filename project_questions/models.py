from django.db import models

# Create your models here.


class Questions(models.Model):
    question = models.TextField(max_length=50, verbose_name='سوال')
    answer = models.TextField(max_length=200, verbose_name='پاسخ')

    class Meta:
        verbose_name = 'سوالات و پاسخ '
        verbose_name_plural = 'سوالات و پاسخ'

    def __str__(self):
        return self.question
