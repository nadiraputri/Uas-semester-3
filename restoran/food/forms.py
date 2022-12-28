from django.forms import ModelForm
from food.models import Menu

class FormMenu(ModelForm):
    class Meta:
        model = Menu
        fields = '__all__'