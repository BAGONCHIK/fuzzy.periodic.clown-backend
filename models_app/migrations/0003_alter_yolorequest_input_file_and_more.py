# Generated by Django 4.2.7 on 2023-12-03 18:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('models_app', '0002_alter_yolorequest_input_file_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='yolorequest',
            name='input_file',
            field=models.FileField(blank=True, null=True, upload_to='', verbose_name='Исходный файл'),
        ),
        migrations.AlterField(
            model_name='yolorequest',
            name='output_file',
            field=models.FileField(blank=True, null=True, upload_to='', verbose_name='Выходной файл'),
        ),
    ]
