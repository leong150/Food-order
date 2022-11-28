from django.forms import ModelForm
from .models import menu
  
  
class menuform(ModelForm):  
    class meta:  
        # To specify the model to be used to create form  
        models = menu
        # It includes all the fields of model  
        fields = '__all__'  