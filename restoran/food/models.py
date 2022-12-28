from django.db import models

# Create your models here.

class Menu(models.Model):
    pesanan = models.CharField(max_length=20)
    jumlah = models.IntegerField(null=True)

    def __str__(self):
        return self.pesanan