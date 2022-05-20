from django.urls import path
from . import views

urlpatterns = [
    path('create/', views.add_items, name='add-items'),
    path('all/', views.view_items, name='view-items'),
    path('update/<int:id>', views.update_items, name='update-items'),
    path('item/<int:id>/delete', views.delete_items, name='delete-items'),
    path('user/<int:user>', views.find_items, name='find_items')
]
