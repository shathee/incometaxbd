from django.urls import path

from . import views

urlpatterns = [
    path('api/zones/', views.ZoneList.as_view() ),
]