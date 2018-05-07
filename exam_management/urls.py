from django.urls import path, include
from . import views
from .views import QuestionAPIView
from rest_framework import routers

# router = routers.DefaultRouter()
# router.register(r'exam',QuestionViewset)

urlpatterns = [
    path('<int:id>/', views.exam_page, name='exam_details'),
    path('', views.home_page, name='home') ,
    path('api/', QuestionAPIView.as_view(), name="questions_api"),   
]