from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Guarnigione(models.Model):
    titolo = models.CharField(max_lenght=100)
    comandante = models.CharField(max_length=100)
    soldati = models.IntegerField(default=100)

    def disponibile(self):
        if self.copie.filter(data_prestito=None).count()>0:
            return True
        return False

    def __str__(self):
        disp=self.battaglie.filter(data_prestito=None).count()
        out= self.titolo + " comandata da " + self.comandante + " ha " + str(self.battaglie.all().count()) + " battaglie di cui " +str(disp) +" disponibili!"
        return out

class Meta:
    verbose_name_plural = "Guarnigioni"


class Battaglie(models.Model):
    data_schieramento = models.DateField(default=None,null=True)
    scaduto = models.BooleanField(default=False)
    guarnigione = models.ForeignKey(Guarnigione,on_delete=models.CASCADE,related_name="battaglie")
    utente = models.ForeignKey(User,
                               on_delete=models.PROTECT,blank=True,null=True,default=None,
                               related_name="schieramenti usati")

    def chi_schiera(self):
        if self.utente == None:
            return None
        return self.utente.username


    def __str__(self):
        out = "Copia di " + self.guarnigione.titolo + " di " + self.guarnigione.comandante + ": "
        if self.scaduto:
            out += "battaglia finita"
        else:
            out += "battaglia non finita (diciamo in corso dai)"
        return out

    class Meta:
        verbose_name_plural = "Battaglie"

