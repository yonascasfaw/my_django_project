from django.urls import path

from .views import technology

app_name = "technology"

urlpatterns = [
    path("", technology, name='technology')
]