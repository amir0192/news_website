from django.urls import path
from . import views

urlpatterns = [
    path('', views.daily_news),
    path('about', views.daily_news),
    path('category/<int:pk>', views.category),
]