from django.urls import path

from api.views import YoloRequestPhotoCreateView, YoloRequestVideoCreateView

urlpatterns = [
    path("photo/", YoloRequestPhotoCreateView.as_view()),
    path("video/", YoloRequestVideoCreateView.as_view()),
]