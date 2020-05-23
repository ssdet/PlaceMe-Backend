from django.urls import path, include
from rest_framework.routers import DefaultRouter, SimpleRouter 
from api.views import *


StudentViewRouter = DefaultRouter()
StudentViewRouter.register(r'StudentData', StudentViewSet, basename='StudentData')

urlpatterns = [
    path('', include('djoser.urls')),
    path('',include('djoser.urls.authtoken')),
    path('userprofile/',UserProfileView.as_view()),
    path('',include(StudentViewRouter.urls)),
    path('Register/Student/',RegisterStudentView.as_view()),
    path('Register/Faculty/',RegisterFacultyView.as_view()),
    path('Register/HR/',RegisterHRView.as_view())
    
   
]
