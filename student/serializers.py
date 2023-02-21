# from rest_framework.serializers import ModelSerializer
# from .models import StudentClass
#
# class StudentSerializer(ModelSerializer):
#     class Meta:
#         model = StudentClass
#         fields = ["name", "roll"]
from rest_framework import serializers
from .models import Book

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = '__all__'
