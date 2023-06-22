from django.db import models
from accounts.models import CustomUser
# Create your models here.

class Coffee (models.Model):
    name = models.CharField(max_length=100,null=False, blank=True)
    price = models.IntegerField(null=False, blank=True)
    desc = models.TextField(null=False, blank=True)
    purchaser = models.ForeignKey(CustomUser, on_delete=models.CASCADE, null=True, blank=True)


    def __str__(self):
        return self.name
    