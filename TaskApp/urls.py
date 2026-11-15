
from django.contrib import admin
from django.urls import path
from .import views


urlpatterns = [
    # path('admin/', admin.site.urls),
    # path('',include('TaskApp.urls'))

    path('users/',views.ListCreateView.as_view(), name="list_user"),
    path('categories/',views.ListCategoryView.as_view(), name= "list_categories"),
    path('tasks/', views.ListTaskView.as_view(),name="list_tasks" )


]
