# Generated by Django 2.0.5 on 2018-05-29 07:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0004_auto_20180529_1535'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='comment',
            options={'verbose_name_plural': '评论'},
        ),
        migrations.AlterModelOptions(
            name='thumbup',
            options={'verbose_name_plural': '点赞'},
        ),
    ]