from django.shortcuts import render
from rest_framework import generics
from .models import User
from .models import Category
from .models import Task
from .serializers import UserSerializers
from .serializers import CategorySerializers,TaskSerializer
from rest_framework import filters
from django_filters.rest_framework import DjangoFilterBackend






#this is to display user view
class ListCreateView(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializers
   

    #Filtering here not working for category
    # def get_queryset(self):
    #     queryset = Category.objects.all()
    #     name = self.request.query_params.get('name')
    #     if name:
    #         queryset = queryset.filter(name__icontains=name)
    #     return queryset

   







# this is to update and display user view
class ListRetriveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    lookup_field = "pk"
    serializer_class = UserSerializers

#This is for user detail view
class UserDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializers





#This is to list category view in the display
class ListCategoryView(generics.ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializers     

    #For Filtering and Searching using pip this works
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    filterset_fields = ['name']
    search_fields = ['name']

# this is to update, retrive and delete  category view
class ListCategoryRetriveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    lookup_field = "pk"
    serializer_class = UserSerializers

#This is for category detail view
class CategoryDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializers



# this is to display list view for Task
class ListTaskView(generics.ListCreateAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer

#this is to retrive update and delete list view for Task

class ListTaskRetriveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Task.objects.all()
    lookup_field = "pk"
    serializer_class = TaskSerializer

#This is for category detail view

class TaskDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer

