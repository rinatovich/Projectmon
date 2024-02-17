from rest_framework import generics
from rest_framework.generics import ListAPIView, ListCreateAPIView
from rest_framework.pagination import PageNumberPagination
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAdminUser

from .models.components import LegalEntity, Document
from .models.person import Person
from .serializers import LegalEntitySerializer, DocumentSerializer, PersonSerializer
from rest_framework.filters import SearchFilter
from django.db.models import Q
from unidecode import unidecode


class StandardResultsSetPagination(PageNumberPagination):
    page_size = 10
    page_size_query_param = 'page_size'
    max_page_size = 20


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
        query = self.request.query_params.get('q', '').strip()
        queryset = Document.objects.all()
        for char in query:
            char_upper = char.upper()
            char_lower = char.lower()
            char_unidecode = unidecode(char)
            queryset = queryset.filter(
                Q(title__icontains=char_upper) | Q(title__icontains=char_lower) |
                Q(document_type__icontains=char_upper) | Q(document_type__icontains=char_lower) |
                Q(title__icontains=char_unidecode) | Q(document_type__icontains=char_unidecode)
            )
        return queryset.distinct()


class DocumentAPIDestroy(generics.RetrieveDestroyAPIView):
    queryset = Document.objects.all()
    serializer_class = DocumentSerializer
    permission_classes = (IsAdminUser,)


class PersonListCreateAPIView(generics.ListCreateAPIView):
    queryset = Person.objects.all()
    serializer_class = PersonSerializer
    pagination_class = StandardResultsSetPagination


class PersonRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Person.objects.all()
    serializer_class = PersonSerializer
