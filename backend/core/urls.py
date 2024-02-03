from django.urls import path
from .views import *


urlpatterns = [
    path('persons/', PersonListCreateView.as_view(), name='person-list-create'),
    path('persons/<int:pk>/', PersonDetailView.as_view(), name='person-detail'),
    path('employees/', EmployeeListCreateView.as_view(), name='person-list-create'),
    path('employees/<int:pk>/', EmployeeDetailView.as_view(), name='person-detail'),
]