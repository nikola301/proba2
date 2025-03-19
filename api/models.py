from django.db import models

# Create your models here.

class Helikopteri(models.Model):
    h_id = models.IntegerField(primary_key=True)
    tip = models.CharField(max_length=20)
    tip_resursa = models.CharField(max_length=5, blank=True, null=True)
    serijski_broj = models.CharField(max_length=20)
    reg_oznaka = models.CharField(max_length=6)
    datum_proizvodnje = models.DateField(blank=True, null=True)
    broj_oo = models.IntegerField(blank=True, null=True)
    nalet_do_oo = models.DecimalField(max_digits=8, decimal_places=2, blank=True, null=True)    
    crr_do = models.DecimalField(max_digits=8, decimal_places=2, blank=True, null=True)     
    datum_zadnje_oo = models.DateField(blank=True, null=True )
    vrr_do = models.DateField(blank=True, null=True )
    ukupan_nalet = models.PositiveIntegerField(blank=True, null=True )
    status = models.PositiveIntegerField(blank=True, null=True )
    gorivo = models.PositiveIntegerField(blank=True, null=True )
    vrsta = models.CharField(max_length=25, blank=True, null=True )
    tehnicar = models.CharField(max_length=55, blank=True, null=True )
    dm = models.CharField(max_length=1, blank=True, null=True )
    kv = models.DecimalField(max_digits=3, decimal_places=2, blank=True, null=True )
    napomena = models.CharField(max_length=300, blank=True, null=True )
    tip_opsti = models.CharField(max_length=15, blank=True, null=True )
    ostatak_h = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True )    
    ostatak_d = models.DateField(blank=True, null=True )
    sletanja = models.IntegerField(blank=True, null=True )
    azurirano = models.DateTimeField(blank=True, null=True )
    elt_fixni = models.CharField(max_length=15, blank=True, null=True)
    elt_portable = models.CharField(max_length=15, blank=True, null=True)
    vazduh = models.PositiveIntegerField(blank=True, null=True)
    zemlja = models.PositiveIntegerField(blank=True, null=True)
    transponder_24bit = models.CharField(max_length=255, blank=True, null=True)
    ostatak_sletanja = models.IntegerField(blank=True, null=True)

    def __str__(self):
      return self.reg_oznaka



    class Meta:
        managed = False
        db_table = 'helikopteri'

