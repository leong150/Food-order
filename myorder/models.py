from django.db import models
from django.forms import ModelForm

# Create your models here.

class Order(models.Model):
    order_no = models.PositiveIntegerField()
    sum = models.DecimalField(max_digits=6, decimal_places=2, default=0)
    STATUS = (
		('P','Pending'),
		('C','Completed')
	)
    status = models.CharField(max_length=1, choices=STATUS, default = 'P')

    def __str__(self):
        return 'Order no. = %s' %(self.order_no) + '\n' +'Total = RM %s' %(self.sum) + '\n' +'Status: %s' %(self.status)

class Menu(models.Model):
    name = models.CharField(max_length=50)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    description = models.TextField()
    image = models.ImageField()

    def __str__(self):
        return '%s (%s)' %(self.name, self.price)

class menuform(ModelForm):  
    class Meta:
        model = Menu  
        fields = ["name", "price", "description", "image"]

class Cart(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, null=True)
    menu = models.ForeignKey(Menu, on_delete=models.CASCADE, null=True)
    qty = models.PositiveIntegerField(default=0)
    
    def __str__(self):
        return '%s x%s' %(self.menu.name, self.qty)
    
    @property
    def total_cost(self):
        return self.qty*self.menu.price