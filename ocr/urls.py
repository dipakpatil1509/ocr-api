from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'ocr/', views.imageToText, name="imageToText"),
]
