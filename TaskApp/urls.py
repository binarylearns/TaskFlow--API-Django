from django.urls import path
from . import views

urlpatterns = [
    # Users
    path('users/', views.ListCreateView.as_view(), name='list_user'),
    path('users/<int:pk>/', views.UserDetailView.as_view(), name='user_detail'),

    # Categories
    path('categories/', views.ListCategoryView.as_view(), name='list_categories'),
    path('categories/<int:pk>/', views.CategoryDetailView.as_view(), name='category_detail'),

    # Tasks
    path('tasks/', views.ListTaskView.as_view(), name='list_tasks'),
    path('tasks/<int:pk>/', views.TaskDetailView.as_view(), name='task_detail'),
]