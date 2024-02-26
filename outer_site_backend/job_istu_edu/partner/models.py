from django.db import models

# Create your models here.


class Document(models.Model):
    """
    Документ
    """
    name = models.CharField(max_length=255)
    url = models.URLField(max_length=500)
    partner = models.ForeignKey("partner.Partner", on_delete=models.CASCADE)


class Direction(models.Model):
    """
    Направление которые ведут партнеры
    """
    name = models.CharField(max_length=255)
    partner = models.ForeignKey(to="partner.Partner", on_delete=models.DO_NOTHING,null=True)


class Partner(models.Model):
    """
    Партнер
    """
    user = models.ForeignKey("auth.User", on_delete=models.CASCADE,null=True)
    name = models.CharField(max_length=255)
    full_name = models.CharField(max_length=255)
    image = models.ImageField(upload_to='files/images')
    site_url = models.URLField()
    invite_url = models.URLField(max_length=255)
    specialities = models.ManyToManyField("infrastructure.Speciality", through="partner.PartnerSpeciality")
    

class PracticeTopic(models.Model):
    name = models.TextField()
    partner = models.ForeignKey(Partner, on_delete=models.CASCADE)


class PartnerSpeciality(models.Model):
    """
    Промежуточная табличка
    """
    speciality = models.ForeignKey("infrastructure.Speciality", on_delete=models.CASCADE)
    parnter = models.ForeignKey(Partner,on_delete=models.CASCADE)