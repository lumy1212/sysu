# Generated by Django 2.0.5 on 2018-07-10 10:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0011_comment_floor'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comment',
            name='reply',
        ),
        migrations.AlterField(
            model_name='comment',
            name='floor',
            field=models.IntegerField(verbose_name='楼层'),
        ),
    ]
