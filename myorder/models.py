from django.db import models
from django.forms import ModelForm

# Create your models here.

class menu(models.Model):
    name = models.CharField(max_length=50)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    description = models.TextField()
    image = models.ImageField()

    def __str__(self):
        return '%s (%s)' %(self.name, self.price)

class menuform(ModelForm):  
    class Meta:  
        # To specify the model to be used to create form  
        model = menu
        # It includes all the fields of model  
        fields = ["name", "price", "description", "image"]