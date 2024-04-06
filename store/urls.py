from django.urls import path
from . import views


#url patterns 
urlpatterns = [
    path('add-item/', views.add_item, name='add-item'),
    path('update-item/<int:pk>/', views.update_item, name='update-item'),
    path('all-items/', views.all_Items, name='all-items'),
    path('delete-item/<int:pk>/', views.delete_item, name='delete-item'),
    path('issue-item/', views.issue_item, name='issue-item'),
    path('issue-history/', views.issue_history, name='issue-history'),
    path('return-item/', views.return_item, name='return-item'),
    path('return-history/', views.return_history, name='return-history'),
    path('restock-item/', views.restockItem, name='restock-item'),
    path('restock-history/', views.restock_history, name='restock-history')
]