from django.db import models
from django.forms import ModelForm

# Create your models here.

class Cart(models.Model):
    order_no = models.PositiveIntegerField(default=1)
    sum = models.DecimalField(max_digits=6, decimal_places=2, default=0)

    def __str__(self):
        return 'Order no. = %s' %(self.order_no) + '\n' +'Total = RM %s' %(self.sum)

class menu(models.Model):
    name = models.CharField(max_length=50)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    description = models.TextField()
    image = models.ImageField()
    qty = models.PositiveIntegerField(default=0)
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return '%s (%s)' %(self.name, self.price)
    
    @property
    def total_cost(self):
        return self.qty * self.price

class menuform(ModelForm):  
    class Meta:  
        # To specify the model to be used to create form  
        model = menu
        # It includes all the fields of model  
        fields = ["name", "price", "description", "image"]
