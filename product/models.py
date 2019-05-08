from django.db import models

# Create your models here.
class Product(models.Model):
    title      = models.CharField(max_length=120)
    decription = models.TextField(blank=True, null= True)
    price      = models.DecimalField(decimal_places=2, max_digits=10000)
    image      = models.ImageField(null=False)
    summary    = models.TextField()
    def __str__(self):
        return  self.title