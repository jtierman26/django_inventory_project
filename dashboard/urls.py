from django.urls import path
from . import views

#url pattern for dashboard
urlpatterns = [
    path('', views.dashboard, name='dashboard')
]