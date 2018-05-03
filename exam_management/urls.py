from django.urls import path, include
from . import views

urlpatterns = [
    path('<int:id>/', views.exam_page, name='exam_details'),
    path('', views.home_page, name='home') ,
]