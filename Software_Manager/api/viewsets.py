from rest_framework import viewsets
from Software_Manager.api import serializers
from Software_Manager import models

class EmployeeViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.EmployeeSerializer
    queryset = models.Employee.objects.all()