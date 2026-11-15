from django.shortcuts import render
from rest_framework import generics
from .models import User
from .models import Category
from .models import Task
from .serializers import UserSerializers
from .serializers import CategorySerializers,TaskSerializer



# Create your views here.

class ListCreateView(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializers






class ListCategoryView(generics.ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializers     



class ListTaskView(generics.ListCreateAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer