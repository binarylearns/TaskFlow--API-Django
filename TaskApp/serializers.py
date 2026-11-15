from rest_framework import serializers
from .models import User
from .models import Category
from .models import Task

class UserSerializers(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = "__all__"



class CategorySerializers(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = "__all__"

class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = "__all__"