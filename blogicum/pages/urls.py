from django.urls import path
from . import views


app_name = 'pages'

urlpatterns = [
    path('about/', views.about),
    path('rules/', views.rules),
]
