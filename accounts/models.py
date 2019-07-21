

from django.db import models

# Create your models here.
class Country(models.Model):
    id = models.IntegerField(unique= True,   primary_key = True)
    Country_name = models.CharField(max_length =20,default=0)

    Country_code = models.IntegerField(default=0)


    def __str__(self):
        return "__all__"

