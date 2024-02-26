from django.db import models

# Create your models here.
class Profession(models.Model):
    """
    Должности/Професии
    """
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name
    

class Speciality(models.Model):
    """
    Специальность
    """
    name = models.CharField(max_length=255)
    

    def __str__(self):
        return self.name


class InstituteSpeciality(models.Model):
    """
    Промежуточная табличка
    """
    institute = models.ForeignKey("infrastucture.Institute",on_delete=models.CASCADE)
    speciality = models.ForeignKey(Speciality, on_delete=models.CASCADE)


class InstituteProfession(models.Model):
    """
    Промежуточная табличка
    """
    institute = models.ForeignKey("infrastucture.Institute",on_delete=models.CASCADE)
    profession = models.ForeignKey(Profession, on_delete=models.CASCADE)


class Institute(models.Model):
    """
    Институт
    """
    name = models.CharField(max_length=255)
    specialities = models.ManyToManyField(Speciality, through=InstituteSpeciality)
    professions = models.ManyToManyField(Profession, through=InstituteProfession)
