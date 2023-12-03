from django.shortcuts import render
from rest_framework.generics import ListAPIView,CreateAPIView,RetrieveUpdateDestroyAPIView,ListCreateAPIView,GenericAPIView
from infrastucture.models import Institute, InstituteProfession, InstituteSpeciality,Profession,Speciality
from infrastucture.serializers import InstituteProfessionSerializer, InstituteSerializer, InstituteSpecialitySerializer, ProfessionSerializer,SpecialitySerializer

# Create your views here.
class InstituteListView(ListAPIView):
    """
    Получения списка всех институтов
    """
    queryset = Institute.objects.all()
    serializer_class = InstituteSerializer


class InstituteCreateView(CreateAPIView):
    """
    Добавление института
    """
    queryset = Institute.objects.all()
    serializer_class = InstituteSerializer


class InstituteSingleView(RetrieveUpdateDestroyAPIView):
    """
    Изменение/удаление института
    """
    queryset = Institute.objects.all()
    serializer_class = InstituteSerializer


class ProfessionListView(ListAPIView):
    """
    Получения списка всех профессий
    """
    queryset = Profession.objects.all()
    serializer_class = ProfessionSerializer


class ProfessionCreateView(CreateAPIView):
    """
    Добавление профессии 
    """
    queryset = Profession.objects.all()
    serializer_class = ProfessionSerializer


class ProfessionSingleView(RetrieveUpdateDestroyAPIView):
    """
    Изменение/удаление профессии 
    """
    queryset = Profession.objects.all()
    serializer_class = ProfessionSerializer


class SpecialityListView(ListAPIView):
    """
    Получения списка всех специальностей
    """
    queryset = Speciality.objects.all()
    serializer_class = SpecialitySerializer


class SpecialityCreateView(CreateAPIView):
    """
    Добавление специальности 
    """
    queryset = Speciality.objects.all()
    serializer_class = SpecialitySerializer


class SpecialitySingleView(RetrieveUpdateDestroyAPIView):
    """
    Изменение/удаление специальности 
    """
    queryset = Speciality.objects.all()
    serializer_class = SpecialitySerializer



class InstituteSpecialityCreate(ListCreateAPIView):
    """
    Добавление специальностей в институт
    """
    queryset = InstituteSpeciality.objects.all()
    serializer_class = InstituteSpecialitySerializer
        

class InstituteProfessionCreate(ListCreateAPIView):
    """
    Добавление специальностей в институт
    """
    queryset = InstituteProfession.objects.all()
    serializer_class = InstituteProfessionSerializer
        
class ManySpecialityInstitute(CreateAPIView):
    """
    Добавления множества 
    """
    serializer_class = SpecialitySerializer

    def post(self,request,pk):
        queryset = Institute.objects.filter(pk=pk)
        serializer = self.get_serializer()
        data = serializer(request[data],many=True)


