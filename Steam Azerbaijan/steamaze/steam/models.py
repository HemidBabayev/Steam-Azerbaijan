from django.db import models
from django.core.validators import MaxLengthValidator, MinLengthValidator


# Create your models here.
class GameShop(models.Model):
    author = models.ForeignKey("auth.User", on_delete = models.CASCADE, verbose_name = "Muellif")
    title = models.CharField(max_length = 50, verbose_name = "Baslik")
    content = models.TextField(max_length= 500, verbose_name = "Metn")
    created_data = models.DateTimeField(auto_now_add=True, verbose_name = "Yaranma Tarixi")
    price = models.FloatField(verbose_name = "Qiymet")
    
    def __str__(self) -> str:
        return f"{self.title} {self.price} AZN"