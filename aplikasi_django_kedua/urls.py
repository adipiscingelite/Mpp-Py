from django.urls import path, include
from . import views  # Mengimport view yang sudah Anda definisikan

app_name = 'kedua'

urlpatterns = [
    path('woii/', views.indexp, name='indexp'),
]
