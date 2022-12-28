from django.forms import ModelForm
from cemilan.models import Cemilan

class FormCemilan(ModelForm):
    class Meta:
        model = Cemilan
        fields = '__all__'