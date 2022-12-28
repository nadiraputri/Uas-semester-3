from django.forms import ModelForm
from drink.models import Minuman

class FormMinuman(ModelForm):
    class Meta:
        model = Minuman
        fields = '__all__'