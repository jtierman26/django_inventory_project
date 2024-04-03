from django.urls import path
from . import views

#urlpatterns for login and logout path
urlpatterns = [
    path('login/', views.login_employee, name='login'),
    path('logout/', views.logout_employee, name='logout')
]