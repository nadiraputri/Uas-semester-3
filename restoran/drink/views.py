from django.shortcuts import render
from drink.models import Minuman
from drink.forms import FormMinuman

def dua(request):
    minuman = Minuman.objects.all()

    konteks = {
        'minuman' : minuman,
    }
    return render(request,'drink/dua.html', konteks)

def plus(request):
    form = FormMinuman()

    konteks = {
        'form': form,
    }

    return render(request, 'drink/plus.html', konteks)
