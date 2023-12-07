from django.contrib import admin

from models_app.models import YoloRequest


@admin.register(YoloRequest)
class YoloRequestAdmin(admin.ModelAdmin):
    pass
