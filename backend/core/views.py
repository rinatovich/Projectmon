from rest_framework import generics
from rest_framework.generics import ListAPIView, ListCreateAPIView
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAdminUser

from .models.components import LegalEntity, Document
from .models.person import Person
from .serializers import LegalEntitySerializer, DocumentSerializer, PersonSerializer
from rest_framework.filters import SearchFilter
from django.db.models import Q


class LegalEntityListView(ListAPIView):
    queryset = LegalEntity.objects.all()
    serializer_class = LegalEntitySerializer


class DocumentListView(ListCreateAPIView):
    queryset = Document.objects.all()
    serializer_class = DocumentSerializer
    filter_backends = [SearchFilter]
    search_fields = ['title']
    permission_classes = (IsAuthenticatedOrReadOnly,)

    def get_queryset(self):
        query = self.request.query_params.get('q', '').upper()
        return Document.objects.filter(
            Q(title__icontains=query) | Q(title__icontains=query.lower()) | Q(document_type__icontains=query) | Q(
                document_type__icontains=query.lower()))


class DocumentAPIDestroy(generics.RetrieveDestroyAPIView):
    queryset = Document.objects.all()
    serializer_class = DocumentSerializer
    permission_classes = (IsAdminUser,)


class PersonListCreateAPIView(generics.ListCreateAPIView):
    queryset = Person.objects.all()
    serializer_class = PersonSerializer


class PersonRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Person.objects.all()
    serializer_class = PersonSerializer
