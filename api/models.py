from django.db import models

# Create your models here.

class Helikopteri(models.Model):
    h_id = models.IntegerField(primary_key=True, db_comment='0')
    tip = models.CharField(max_length=20, db_comment='1')
    tip_resursa = models.CharField(max_length=5, blank=True, null=True, db_comment='2')
    serijski_broj = models.CharField(max_length=20, db_comment='3')
    reg_oznaka = models.CharField(max_length=6, db_comment='4')
    datum_proizvodnje = models.DateField(blank=True, null=True, db_comment='5')
    broj_oo = models.IntegerField(blank=True, null=True, db_comment='6')
    nalet_do_oo = models.DecimalField(max_digits=8, decimal_places=2, blank=True, null=True, db_comment='7')    
    crr_do = models.DecimalField(max_digits=8, decimal_places=2, blank=True, null=True, db_comment='8')     
    datum_zadnje_oo = models.DateField(blank=True, null=True, db_comment='9')
    vrr_do = models.DateField(blank=True, null=True, db_comment='10')
    ukupan_nalet = models.PositiveIntegerField(blank=True, null=True, db_comment='11')
    status = models.PositiveIntegerField(blank=True, null=True, db_comment='12')
    gorivo = models.PositiveIntegerField(blank=True, null=True, db_comment='13')
    vrsta = models.CharField(max_length=25, blank=True, null=True, db_comment='14')
    tehnicar = models.CharField(max_length=55, blank=True, null=True, db_comment='16')
    dm = models.CharField(max_length=1, blank=True, null=True, db_comment='17. decimalni ili minutni obračun')
    kv = models.DecimalField(max_digits=3, decimal_places=2, blank=True, null=True, db_comment='18. koeficijen vazduha npr 20%vazduha je 0,2')
    napomena = models.CharField(max_length=300, blank=True, null=True, db_comment='19')
    tip_opsti = models.CharField(max_length=15, blank=True, null=True, db_comment='20')
    ostatak_h = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True, db_comment='21')    
    ostatak_d = models.DateField(blank=True, null=True, db_comment='22')
    sletanja = models.IntegerField(blank=True, null=True, db_comment='23')
    azurirano = models.DateTimeField(blank=True, null=True, db_comment='25')
    elt_fixni = models.CharField(max_length=15, blank=True, null=True, db_comment='26')
    elt_portable = models.CharField(max_length=15, blank=True, null=True, db_comment='27')
    vazduh = models.PositiveIntegerField(blank=True, null=True, db_comment='28')
    zemlja = models.PositiveIntegerField(blank=True, null=True, db_comment='29')
    transponder_24bit = models.CharField(max_length=255, blank=True, null=True, db_comment='30')
    ostatak_sletanja = models.IntegerField(blank=True, null=True, db_comment='31')

    def __str__(self):
      return self.reg_oznaka



    class Meta:
        managed = False
        db_table = 'helikopteri'
        db_table_comment = 'Podaci o helikopterima'

