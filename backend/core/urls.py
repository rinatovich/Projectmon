from django.urls import path
from .views import *

urlpatterns = [
    path('legal-entities/', LegalEntityListView.as_view(), name='legal-entities-list'),
    path('documents/', DocumentListView.as_view(), name='document-list'),
]
