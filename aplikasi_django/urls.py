from django.urls import path
from . import views

app_name = 'app_name_pertama'

urlpatterns = [
    path('', views.index, name='index'),
    # path('/', views., name=''),
    path('home/', views.home, name='home'),
]

# app_name = 'app_name_kedua'

# urlpatterns = [
#     path('kedua/', views.index, name='index_kedua'),
# ]
