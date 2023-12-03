from rest_framework.generics import CreateAPIView,ListAPIView,RetrieveUpdateDestroyAPIView
from partner.models import Document, Partner
from partner.serializers import DocumentSerializer, PartnerSerializer
# Create your views here.

class DocumentCreateView(CreateAPIView):
    queryset = Document.objects.all()
    serializer_class = DocumentSerializer


class DocumentListView(ListAPIView):
    queryset = Document.objects.all()
    serializer_class = DocumentSerializer


class DocumentSingleView(RetrieveUpdateDestroyAPIView):
    queryset = Document.objects.all()
    serializer_class = DocumentSerializer
    
class PartnerCreateView(CreateAPIView):
    queryset = Partner.objects.all()
    serializer_class = PartnerSerializer


class PartnerListView(ListAPIView):
    queryset = Partner.objects.all()
    serializer_class = PartnerSerializer


class PartnerSingleView(RetrieveUpdateDestroyAPIView):
    queryset = Partner.objects.all()
    serializer_class = PartnerSerializer

    