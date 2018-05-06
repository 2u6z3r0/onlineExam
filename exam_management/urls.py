from django.urls import path, include
from . import views
from .views import QuestionViewset
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'exam',QuestionViewset)

urlpatterns = [
    path('<int:id>/', views.exam_page, name='exam_details'),
    path('', views.home_page, name='home') ,
    path('api/', include(router.urls)),   
]