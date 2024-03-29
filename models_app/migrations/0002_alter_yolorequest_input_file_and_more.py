# Generated by Django 4.2.7 on 2023-12-03 18:36

from django.db import migrations, models
import utils.file_uploader


class Migration(migrations.Migration):

    dependencies = [
        ('models_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='yolorequest',
            name='input_file',
            field=models.FileField(blank=True, null=True, upload_to=utils.file_uploader.uploaded_file_path, verbose_name='Исходный файл'),
        ),
        migrations.AlterField(
            model_name='yolorequest',
            name='output_file',
            field=models.FileField(blank=True, null=True, upload_to=utils.file_uploader.uploaded_file_path, verbose_name='Выходной файл'),
        ),
    ]
