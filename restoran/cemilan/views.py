from django.shortcuts import render
from cemilan.models import Cemilan
from cemilan.forms import FormCemilan

def tiga(request):
    cemilan = Cemilan.objects.all()

    konteks = {
        'cemilan' : cemilan,
    }
    return render(request,'cemilan/tiga.html', konteks)

def minus(request):
    form = FormCemilan()

    konteks = {
        'form': form,
    }

    return render(request, 'drink/plus.html', konteks)

