
from django.contrib import admin
from django.urls import path
from . import views as v

urlpatterns = [
    path('',v.CreateOutsourcing.as_view()),
    path('<int:pk>',v.RetriveOutsourcing.as_view()),
]
