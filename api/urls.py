from django.urls import path
from api import views

urlpatterns = [
    path('get', views.RestAPIView.as_view()),
]
