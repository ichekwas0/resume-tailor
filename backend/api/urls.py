from django.shortcuts import render
from users.views import CreateUserView, RetrieveUserView
# Create your views here.
from ai.views import AITailorResumeView

from django.urls import path, include

urlpatterns = [
    path("users/", CreateUserView.as_view(), name='create-user'),
    path("users/<uuid:id>", RetrieveUserView.as_view(), name='retrieve-user'),
    path("users/<uuid:id>/tailor", AITailorResumeView.as_view(), name='tailor-user-resume')
]
