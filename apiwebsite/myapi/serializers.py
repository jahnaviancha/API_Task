from rest_framework import serializers
from .models import Student


class StudentSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model=Student
        fields=('roll_no', 'name', 'department', 'stud_class')
