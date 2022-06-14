# Generated by Django 3.2.13 on 2022-06-14 18:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('project_blog', '0013_comment_email'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='name',
            field=models.CharField(default='name', max_length=10, verbose_name='نام و نام خانوادگی'),
        ),
        migrations.AlterField(
            model_name='comment',
            name='body',
            field=models.TextField(default='default', max_length=200, verbose_name='متن '),
        ),
        migrations.AlterField(
            model_name='comment',
            name='email',
            field=models.EmailField(default='email', max_length=254, verbose_name='ایمیل'),
        ),
    ]