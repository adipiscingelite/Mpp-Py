from django.urls import path, include
from . import views

app_name = 'pertama'

urlpatterns = [
    path('', views.index, name='index'),
    path('home/', views.home, name='home'),
    path('kedua/', include('aplikasi_django_kedua.urls')),
]
