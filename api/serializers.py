from rest_framework import serializers

from models_app.models import YoloRequest


class YoloRequestCreateSerializer(serializers.ModelSerializer):
    input_file = serializers.FileField()

    class Meta:
        model = YoloRequest
        fields = ["input_file", ]


class YoloRequestSerializer(serializers.ModelSerializer):

    class Meta:
        model = YoloRequest
        fields = "__all__"
