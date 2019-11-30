from django.db import models

class FinancialYear(models.Model):
    year           =   models.IntegerField('سال مالی')
    is_deleted     =   models.BooleanField()
    description    =   models.TextField('توضیحات')

    def __str__(self):
        return str(self.year)

class City(models.Model):
    name            =   models.CharField('نام شهر', max_length=50)

    def __str__(self):
        return self.name

class Bank(models.Model):
    title           =   models.CharField('نام بانک',max_length=50)
    branch_name     =   models.CharField('نام شعبه',max_length=50)
    account_number   =   models.CharField('شماره حساب',max_length=50)
    shaba_number    =   models.CharField('شماره شبا',max_length=27)

    def __str__(self):
        return "{}-{}".format(self.title,self.account_number)
        

class Employer(models.Model):
    title           =   models.CharField('نام کارفرما',max_length=50)
    national_code   =   models.CharField('شناسه ملی',max_length=11)
    economic_id     =   models.CharField('شماره اقتصادی',max_length=11)
    phone_number    =   models.CharField("شماره تلفن",max_length=11)
    city_name       =   models.ForeignKey(City,verbose_name="شهر",null=True,on_delete=models.SET_NULL)
    address         =   models.TextField(verbose_name="آدرس")
    description     =   models.CharField('توضیحات',max_length=100,null=True,blank=True)

    def get_abseloute_url(self):
        return f"/employers/{self.id}"

    def __str__(self):
        return self.title


class Contract(models.Model):
    employer    =   models.ForeignKey(Employer,verbose_name="کارفرما",on_delete=models.CASCADE)
    title       =   models.CharField('عنوان قرارداد',max_length=100)
    number      =   models.CharField('شماره قرارداد',max_length=50)
    date        =   models.DateField('تاریخ شروع',)
    end_date    =   models.DateField('تاریخ پایان',null=True,blank=True)
    gross_amount=   models.DecimalField('مبلغ اولیه قرارداد',max_digits=20,decimal_places=2,default=0)
    adjustment_amount=   models.DecimalField('مبلغ تعدیل',max_digits=20,decimal_places=2,default=0)
    final_amount=   models.DecimalField('مبلغ نهایی قرارداد',max_digits=20,decimal_places=2,default=0)
    total_payments=   models.DecimalField('مجموع مبالغ دریافتی',max_digits=20,decimal_places=2,default=0)
    progress    =   models.DecimalField('درصد پیشرفت',max_digits=10,decimal_places=2,default=0)
    scan_file   =   models.FileField('فایل قرارداد',blank=True,upload_to='income/static/contracts')
    description =   models.CharField('توضیحات',blank=True,max_length=100)

    def __str__(self):
        return self.title
