from rest_framework import serializers
from infrastucture.models import Institute, InstituteProfession, InstituteSpeciality,Profession,Speciality

class ProfessionSerializer(serializers.ModelSerializer):

    class Meta:
        model = Profession
        fields = '__all__'


class SpecialitySerializer(serializers.ModelSerializer):

    class Meta:
        model = Speciality
        fields = '__all__'


class InstituteSerializer(serializers.Serializer):
    specialities = serializers.StringRelatedField(many=True)
    professions = serializers.StringRelatedField(many=True)

    class Meta:
        model = Institute
        fields = [
            'name'
        ]
        read_only_fields = [
        "specialities",
        "professions",
        ]


class InstituteProfessionSerializer(serializers.ModelSerializer):

    class Meta:
        model = InstituteProfession
        fields = '__all__'


class InstituteSpecialitySerializer(serializers.ModelSerializer):

    class Meta:
        model = InstituteSpeciality
        fields = '__all__'


