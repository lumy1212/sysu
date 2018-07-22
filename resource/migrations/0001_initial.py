# Generated by Django 2.0.5 on 2018-06-24 17:28

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='MyFile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('filename', models.CharField(max_length=50)),
                ('content', models.FileField(upload_to='upload/data/')),
                ('date_added', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Topic',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.CharField(max_length=30)),
                ('date_added', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.AddField(
            model_name='myfile',
            name='topic',
            field=models.ForeignKey(on_delete=True, to='resource.Topic'),
        ),
        migrations.AddField(
            model_name='myfile',
            name='uploader',
            field=models.ForeignKey(on_delete=True, to=settings.AUTH_USER_MODEL),
        ),
    ]
