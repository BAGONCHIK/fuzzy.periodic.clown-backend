from django.core.files import File
from django.shortcuts import render

# Create your views here.
from drf_yasg.utils import swagger_auto_schema
from rest_framework.generics import CreateAPIView
from rest_framework.parsers import MultiPartParser
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from drf_yasg import openapi
from source.photo import process as process_photo
from source.video import process as process_video

from api.serializers import YoloRequestCreateSerializer, YoloRequestSerializer
from models_app.models import YoloRequest


class YoloRequestPhotoCreateView(CreateAPIView):
    permission_classes = (AllowAny, )
    parser_classes = (MultiPartParser,)

    @swagger_auto_schema(tags=["photo"],
                         operation_description="Process Photo",
                         request_body=YoloRequestCreateSerializer,
                         responses={200: openapi.Response("Success", YoloRequestSerializer)})
    def post(self, request, *args, **kwargs):
        obj = YoloRequest.objects.create(input_file=request.data.get("input_file"))
        file, additional_data = process_photo(obj.input_file.url)
        obj.additional_data = additional_data
        filename, ext = obj.input_file.name.split(".")
        obj.output_file.save(filename + '_processed.' + ext, file, save=True)

        return Response(YoloRequestSerializer(obj).data)


class YoloRequestVideoCreateView(CreateAPIView):
    permission_classes = (AllowAny,)
    parser_classes = (MultiPartParser,)

    @swagger_auto_schema(tags=["video"],
                         operation_description="Process Video",
                         request_body=YoloRequestCreateSerializer,
                         responses={200: openapi.Response("Success", YoloRequestSerializer)})
    def post(self, request, *args, **kwargs):
        obj = YoloRequest.objects.create(input_file=request.data.get("input_file"))
        additional_data = process_video(obj.input_file.url)
        obj.additional_data = additional_data
        filename, ext = obj.input_file.name.split(".")
        with open('media/output.mp4', 'rb') as file:
            obj.output_file.save(filename + '_processed.mp4', File(file), save=False)
        obj.save()

        return Response(YoloRequestSerializer(obj).data)
