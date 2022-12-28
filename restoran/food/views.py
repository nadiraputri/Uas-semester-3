from django.shortcuts import render
from food.models import Menu
from food.forms import FormMenu

def food(request):
    makanan = Menu.objects.all()

    konteks = {
        'makanan' : makanan,
    }
    return render(request, 'food/satu.html', konteks)


def tambah(request):
    form = FormMenu()

    konteks = {
        'form': form,
    }

    return render(request, 'food/tambah.html', konteks)
