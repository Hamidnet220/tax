from django.db import models

class Employeer(models.Model):
    title           =   models.CharField('نام کارفرما',max_length=50)
    national_code   =   models.CharField('شناسه ملی',max_length=11)
    description     =   models.CharField('توضیحات',max_length=100,null=True,blank=True)

    def __str__(self):
        return "{}-{}".format(self.title,self.national_code)

class Bank(models.Model):
    title           =   models.CharField('نام بانک',max_length=50)
    branch_name     =   models.CharField('نام شعبه',max_length=50)
    account_number   =   models.CharField('شماره حساب',max_length=50)
    shaba_number    =   models.CharField('شماره شبا',max_length=27)

    def __str__(self):
        return "{}-{}".format(self.title,self.account_number)

class Contract(models.Model):
    title       =   models.CharField('عنوان قرارداد',max_length=100)
    number      =   models.CharField('شماره قرارداد',max_length=50)
    date        =   models.DateField('تاریخ',)
    gross_amount=   models.DecimalField('مبلغ قرارداد',max_digits=20,decimal_places=2,default=0)
    description =   models.CharField('توضیحات',blank=True,max_length=100)

    def __str__(self):
        return self.title

class Income(models.Model):
    employeer   =   models.ForeignKey(Employeer,verbose_name='کارفرما',on_delete=models.CASCADE)
    contract    =   models.ForeignKey(Contract,verbose_name='قرارداد',max_length=150,on_delete=models.CASCADE)
    year        =   models.IntegerField('سال')
    month       =   models.IntegerField('ماه')
    day         =   models.IntegerField('روز')
    bank        =   models.ForeignKey(Bank,verbose_name='بانک',on_delete=models.CASCADE,null=True,blank=True,default='')
    doc_number  =   models.CharField('شماره سند',max_length=30)
    gross_amount=   models.DecimalField('مبلغ ناخالص',max_digits=20,decimal_places=2)
    VAT_included=   models.BooleanField('مشمول ارزش افزوده میباشد؟',default=True)
    VAT_amount  =   models.DecimalField('مبلغ ارزش افزوده',max_digits=20,decimal_places=2)
    tax_included=   models.BooleanField('مشمول مالیات میباشد؟',default=True)
    tax_amount  =   models.DecimalField('مبلغ مالیات',max_digits=20,decimal_places=2)
    pay_amount  =   models.DecimalField('خالص پرداختی',max_digits=20,decimal_places=2,default=0)
    description =   models.CharField(max_length=100,null=True,blank=True)

    class Meta:
        ordering=['year','month','day']

    def __str__(self):
        return "{}-{}-{}-{}".format(self.year,self.month,self.contract,self.gross_amount)
    


