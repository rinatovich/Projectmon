from django.shortcuts import render

# Create your views here.
from rest_framework import generics, serializers
from rest_framework.pagination import PageNumberPagination
from .models.entities import *
from .serializers import *


class BasePagination(PageNumberPagination):
    page_size_query_param = 'page_size'
    max_page_size = 100
    page_size = 5


class BaseListCreateView(generics.ListCreateAPIView):
    queryset = None  # Переопределите это в подклассах
    serializer_class = None  # Переопределите это в подклассах
    pagination_class = BasePagination

    def get_serializer(self, *args, **kwargs):
        kwargs['context'] = self.get_serializer_context()
        kwargs['context']['age'] = True
        return self.serializer_class(*args, **kwargs)


class BaseDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = None  # Переопределите это в подклассах
    serializer_class = None  # Переопределите это в подклассах


class PersonPagination(BasePagination):
    pass


class PersonListCreateView(BaseListCreateView):
    queryset = Person.objects.all()
    serializer_class = PersonSerializer
    pagination_class = PersonPagination


class PersonDetailView(BaseDetailView):
    queryset = Person.objects.all()
    serializer_class = PersonSerializer


class EmployeePagination(BasePagination):
    pass


class EmployeeListCreateView(BaseListCreateView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
    pagination_class = EmployeePagination


class EmployeeDetailView(BaseDetailView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
