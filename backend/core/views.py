from rest_framework.generics import ListAPIView

from .models.components import LegalEntity, Document
from .serializers import LegalEntitySerializer, DocumentSerializer
from rest_framework.filters import SearchFilter
from django.db.models import Q


class LegalEntityListView(ListAPIView):
    queryset = LegalEntity.objects.all()
    serializer_class = LegalEntitySerializer


class DocumentListView(ListAPIView):
    queryset = Document.objects.all()
    serializer_class = DocumentSerializer
    filter_backends = [SearchFilter]
    search_fields = ['title']

    def get_queryset(self):
        query = self.request.query_params.get('q', '').upper()
        return Document.objects.filter(
            Q(title__icontains=query) | Q(title__icontains=query.lower()) | Q(document_type__icontains=query) | Q(document_type__icontains=query.lower()))



