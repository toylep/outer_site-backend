from django.urls import path
from partner.views import(
    DocumentCreateView,
    DocumentListView,
    DocumentSingleView,
    PartnerCreateView,
    PartnerListView,
    PartnerSingleView
)

urlpatterns = [
    path('document/',DocumentCreateView.as_view()),
    path('document/',DocumentListView.as_view()),
    path('document/',DocumentSingleView.as_view()),
    path('',PartnerCreateView.as_view()),
    path('',PartnerListView.as_view()),
    path('',PartnerSingleView.as_view()),

]
