# Generated by Django 2.0.5 on 2018-06-27 07:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0007_auto_20180614_0006'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='reply',
            field=models.TextField(blank=True, default='', verbose_name='回复评论'),
        ),
    ]
