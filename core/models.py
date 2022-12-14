from django.db import models

# Create your models here.
class Rang(models.Model):
    nomi = models.CharField(max_length=31)

    def __str__(self):
        return self.nomi

class Moshina(models.Model):
    nomi = models.CharField(max_length=21)
    rang = models.ForeignKey(Rang, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.nomi