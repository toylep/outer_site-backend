from infrastucture.views import(
    ProfessionCreateView,
    ProfessionListView,
    ProfessionSingleView,
    SpecialityCreateView,
    SpecialityListView,
    SpecialitySingleView
)
from django.urls import path


urlpatterns = [
    path('speciality/',SpecialityListView.as_view()),
    path('speciality/',SpecialityCreateView.as_view()),
    path('speciality/',SpecialitySingleView.as_view()),
    path('profession/',ProfessionListView.as_view()),
    path('profession/',ProfessionCreateView.as_view()),
    path('profession/',ProfessionSingleView.as_view()),
]
