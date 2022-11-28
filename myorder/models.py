from django.db import models

# Create your models here.

class menu(models.Model):
    name = models.CharField(max_length=50)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    description = models.TextField()
    image = models.ImageField()

    def __str__(self):
        return '%s (%s)' %(self.name, self.price)