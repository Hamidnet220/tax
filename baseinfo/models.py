from django.db import models
from django.contrib.auth.admin import User

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


class Guarantee(models.Model):
    GUARANTEE_TYPE=[
        (1," ضمانت نامه شرکت در مناقصه"),
        (2," ضمانت نامه پیش پرداخت"),
        (3," ضمانت نامه حسن انجام کار"),
    ]

    GUARANTEE_STATUS=[
        (1,"صدور"),
        (2,"ابطال شد"),
        (3,"تمدید"),
        
    ]
    
    employer        = models.ForeignKey(Employer,verbose_name="کارفرما",on_delete = models.DO_NOTHING)
    contract        = models.ForeignKey(Contract,verbose_name="عنوان قرارداد",on_delete=models.CASCADE)
    guarantee_type  = models.IntegerField("عنوان ضمانت نامه",choices=GUARANTEE_TYPE)
    guarntee_number = models.CharField("شماره ضمانت نامه",max_length=60,blank=True,null=True)
    guarntee_Sepam  = models.CharField("شماره سپام",max_length=60,blank=True,null=True)
    bank            = models.ForeignKey(Bank,verbose_name="نام بانک",on_delete=models.DO_NOTHING) 
    amount          = models.DecimalField("مبلغ ضمانت نامه",max_digits=20,decimal_places=0,default=0)
    status          = models.IntegerField("وضعیت ضمانت نامه",choices=GUARANTEE_STATUS)
    parent_guarantee = models.ForeignKey("self",verbose_name= "ضمانت نامه اصلی",
                    on_delete=models.DO_NOTHING,null=True,blank=True)
    issue_date   = models.DateField("تاریخ صدور")
    expire_date  = models.DateField("تاریخ انقضاء")
    guarantee_file = models.FileField("فایل ضمانت نامه",blank=True,null=True)
    added_by     = models.ForeignKey(User,verbose_name="ایجاد کننده",on_delete=models.DO_NOTHING)

    def __str__(self):
        return f"{self.get_guarantee_type_display()}-{self.contract}"

class CompanyInfo(models.Model):
    name            =   models.CharField('نام شرکت',max_length=50)
    register_number =   models.CharField('شماره ثبت',max_length=20)
    register_date   =   models.DateField('')
    national_code   =   models.CharField('شناسه ملی',max_length=11)
    economic_id     =   models.CharField('شماره اقتصادی',max_length=12)
    phone_number    =   models.CharField("شماره تلفن",max_length=11)
    city_name       =   models.ForeignKey(City,verbose_name="شهر",null=True,on_delete=models.SET_NULL)
    address         =   models.TextField(verbose_name="آدرس")
    email           =   models.EmailField("ایمیل",blank=True,null=True)
    site            =   models.URLField("آدرس سایت",blank=True,null=True)
    description     =   models.CharField('توضیحات',max_length=100,null=True,blank=True)

    def __str__(self):
        return f"{self.name}"

class Person(models.Model):
    POSITION=[
        (1,"مدیرعامل"),
        (2,"رییس هییت مدیره"),
        (3,"نایب رییس هییت مدیره"),
        (4,"عضور"),
        ]
    DEGREE=[
        (1,"دیپلم"),
        (2,"کاردانی"),
        (3,"کارشناسی"),
        (4,"کارشناسی ارشد"),
        ]
    FIELD_OF_STUDY=[
        (1,"عمران"),
        (2,"مکانیک"),
        (3,"کامپیوتر"),
        (4,"برق"),
        (5,"معماری"),
    ]
    company         =   models.ForeignKey(CompanyInfo,verbose_name="نام شرکت",on_delete=models.DO_NOTHING)
    fname           =   models.CharField("نام",max_length=50)
    lname           =   models.CharField("نام خانوادگی",max_length=50)
    father_name     =   models.CharField("نام پدر",max_length=50)
    national_code   =   models.CharField("کد ملی",max_length=10)
    id_number       =   models.CharField("شماره شناسنامه",max_length=10)
    position        =   models.IntegerField("سمت",choices=POSITION)
    degree          =   models.IntegerField("مدرک تحصیلی",choices=DEGREE)
    work_experience =   models.IntegerField("سابقه کار")
    field_of_study  =   models.IntegerField("",choices=FIELD_OF_STUDY)
    tel             =   models.CharField("شماره تلفن",max_length=20,blank=True,null=True)
    address         =   models.TextField("آدرس",blank=True,null=True)
    is_deleted      =   models.BooleanField(default=False)

    def __str__(self):
        return f"{self.fname}-{self.lname}"
