from django.db import models

from django.db import models


class HesabKol(models.Model):
    title       =       models.CharField(max_length=100)

    def __str__(self):
        return self.title

class HesabMoein(models.Model):
    hesab_kol   =       models.ForeignKey(HesabKol,on_delete=models.CASCADE)
    title       =       models.CharField(max_length=100)

    def __str__(self):
        return self.title

class HesabTafzili(models.Model):
    hesb_moien   =      models.ForeignKey(HesabMoein,on_delete=models.CASCADE)
    title       =       models.CharField(max_length=100)

    def __str__(self):
        return self.title

class Sanad(models.Model):
    hesab_tafzili =     models.ForeignKey(HesabTafzili,on_delete=models.CASCADE)
    title       =       models.CharField(max_length=200)
    year        =       models.IntegerField()
    month       =       models.IntegerField()
    day         =       models.IntegerField()        
    bedehkar    =       models.DecimalField(max_digits=20,decimal_places=2,default=0)
    bestankar   =       models.DecimalField(max_digits=20,decimal_places=2,default=0)


    def __str__(self):
        return '{}-{}-{}-{}-{}-{}'.format(self.title,self.year,self.month,self.day,self.bedehkar,self.bestankar)