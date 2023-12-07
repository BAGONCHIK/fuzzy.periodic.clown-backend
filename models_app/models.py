from django.db import models
from django.db.models.signals import post_save
from django.db.models.signals import pre_save
from utils.file_uploader import save_file
from utils.file_uploader import skip_saving_file
from utils.file_uploader import uploaded_file_path


class YoloRequest(models.Model):
    input_file = models.FileField(null=True, blank=True, verbose_name="Исходный файл")
    output_file = models.FileField(null=True, blank=True, verbose_name="Выходной файл")

    additional_data = models.JSONField(null=True, blank=True, verbose_name="Дополнительные данные")

    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Дата обновления")

    class Meta:
        db_table = "yolo_requests"
        verbose_name = "Запрос"
        verbose_name_plural = "Запросы"

