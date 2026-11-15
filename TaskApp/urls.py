
from django.contrib import admin
from django.urls import path
from .import views


urlpatterns = [
    # path('admin/', admin.site.urls),
    # path('',include('TaskApp.urls'))

   #This is for user view
    path('users/',views.ListCreateView.as_view(), name="list_user"),
    path('users/<int:pk>/',views.ListCreateView.as_view(), name="list_user_update"),
   
   #this is for category view
    path('categories/',views.ListCategoryView.as_view(), name= "list_categories"),
    path('categories/<int:pk>/',views.ListCreateView.as_view(), name="list_categories_update"),
   
   #this is for tasks view
    path('tasks/', views.ListTaskView.as_view(),name="list_tasks" ),
    path('tasks/<int:pk>/',views.ListCreateView.as_view(), name="list_tasks_update"),

]
