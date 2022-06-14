# Generated by Django 3.2.13 on 2022-06-11 11:47

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Questions',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question', models.TextField(max_length=200, verbose_name='سوال')),
                ('answer', models.TextField(max_length=200, verbose_name='پاسخ')),
            ],
            options={
                'verbose_name': 'سوالات و پاسخ ',
                'verbose_name_plural': 'سوالات و پاسخ',
            },
        ),
    ]