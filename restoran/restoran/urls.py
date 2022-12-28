from django.contrib import admin
from django.urls import path, include
from food.views import food, tambah
from drink.views import dua, plus
from cemilan.views import tiga, minus

from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.putri),
    path('food/', include('food.urls')),
    path('drink/', include('drink.urls')),
    path('cemilan/', include('cemilan.urls')),
    path('tambah/', tambah),
    path('plus/', plus),
    path('minus/', minus),
]
