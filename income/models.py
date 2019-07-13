from django.db import models

class Employeer(models.Model):
    title           =   models.CharField('نام کارفرما',max_length=50)
    national_code   =   models.CharField('شناسه ملی',max_length=11)
    description     =   models.CharField('توضیحات',max_length=100,null=True,blank=True)

    def __str__(self):
        return "{}-{}".format(self.title,self.national_code)

class Income(models.Model):
    employeer   =   models.ForeignKey(Employeer,on_delete=models.CASCADE)
    title       =   models.CharField('عنوان قرارداد',max_length=150)
    year        =   models.IntegerField('سال')
    month       =   models.IntegerField('ماه')
    gross_amount=   models.DecimalField('مبلغ ناخالص',max_digits=20,decimal_places=2)
    VAT_included=   models.BooleanField('مشمول ارزش افزوده میباشد؟',default=True)
    VAT_amount  =   models.DecimalField('مبلغ ارزش افزوده',max_digits=20,decimal_places=2)
    tax_included=   models.BooleanField('مشمول مالیات میباشد؟',default=True)
    tax_amount  =   models.DecimalField('مبلغ مالیات',max_digits=20,decimal_places=2)
    description =   models.CharField(max_length=100,null=True,blank=True)

    def __str__(self):
        return "{}-{}-{}-{}".format(self.year,self.month,self.title,self.gross_amount)
    


