from django.db import models

# Create your models here.

class FormDaftar(models.Model):
    nama = models.CharField(max_length=30)
    email = models.EmailField()
    tanggal_lahir = models.DateField()
    gender = models.CharField(
        max_length=10,
    )
    alamat = models.TextField()
    agree = models.BooleanField()

    def __str__(self):
        return "{}. {}".format(self.id, self.nama)