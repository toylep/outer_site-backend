from django.db import models

# Create your models here.


class Document(models.Model):
    """
    Документ
    """
    name = models.CharField(max_length=255)
    file = models.FileField(upload_to='files/documents')
    partner = models.ForeignKey("partner.Partner", on_delete=models.CASCADE)


class Direction(models.Model):
    """
    Направление которые ведут партнеры
    """
    name = models.CharField(max_length=255)
    partner =  models.ForeignKey(to="partner.Partner",on_delete=models.DO_NOTHING,null=True)


class Partner(models.Model):
    """
    Партнер
    """
    user = models.ForeignKey("auth.User",on_delete=models.CASCADE,null=True)
    name = models.CharField(max_length=255)
    full_name = models.CharField(max_length=255)
    image = models.ImageField(upload_to='files/images')
    site_url = models.URLField()
    invite_url = models.URLField(max_length=255)
    



