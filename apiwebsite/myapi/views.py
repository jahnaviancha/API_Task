from django.shortcuts import render
from rest_framework import viewsets
from .serializers import StudentSerializer
from .models import Student


# Create your views here.
class StudentViewSet(viewsets.ModelViewSet):
    queryset=Student.objects.all().order_by('roll_no')
    serializer_class =  StudentSerializer
