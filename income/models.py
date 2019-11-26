from django.db import models
class City(models.Model):
    name            =   models.CharField('نام شهر', max_length=50)

    def __str__(self):
        return self.name

class FinancialYear(models.Model):
    year           =   models.IntegerField('سال مالی')
    is_deleted     =   models.BooleanField()
    description    =   models.TextField('توضیحات')
class Employeer(models.Model):
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

class Bank(models.Model):
    title           =   models.CharField('نام بانک',max_length=50)
    branch_name     =   models.CharField('نام شعبه',max_length=50)
    account_number   =   models.CharField('شماره حساب',max_length=50)
    shaba_number    =   models.CharField('شماره شبا',max_length=27)

    def __str__(self):
        return "{}-{}".format(self.title,self.account_number)

class Contract(models.Model):
    employer    =   models.ForeignKey(Employeer,verbose_name="کارفرما",on_delete=models.CASCADE)
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

class Buy(models.Model):
    YEAR_CHOICES=[
        (1396,'1396'),
        (1397,'1397'),
        (1398,'1398'),
        (1399,'1399'),
        (1400,'1400'),
    ]

    MONTH_CHOICES=[
        (1,'فروردین'),
        (2,'اردیبشت'),
        (3,'خرداد'),
        (3,'تیر'),
        (5,'مرداد'),
        (6,'شهریور'),
        (7,'مهر'),
        (8,'آبان'),
        (9,'آذر'),
        (10,'دی'),
        (11,'بهمن'),
        (12,'اسفند'),
    ]

    DAY_CHOICES=[
        (1,'1'),
        (2,'2'),
        (3,'3'),
        (4,'4'),
        (5,'5'),
        (6,'6'),
        (7,'7'),
        (8,'8'),
        (9,'9'),
        (10,'10'),
        (11,'11'),
        (12,'12'),
        (13,'13'),
        (14,'14'),
        (15,'15'),
        (16,'16'),
        (17,'17'),
        (18,'18'),
        (19,'19'),
        (20,'20'),
        (21,'21'),
        (22,'22'),
        (23,'23'),
        (24,'24'),
        (25,'25'),
        (26,'26'),
        (27,'27'),
        (28,'28'),
        (29,'29'),
        (30,'30'),
        (31,'31'),
    ]

    TAX_STATUS=[
        (True,'مشمول'),
        (False,'معاف')
    ]

    employeer   =   models.ForeignKey(Employeer,verbose_name='کارفرما',on_delete=models.CASCADE)
    contract    =   models.ForeignKey(Contract,verbose_name='قرارداد',max_length=150,on_delete=models.CASCADE)
    seller_fname=   models.CharField('نام',max_length=50,blank=True)
    seller_lname=   models.CharField('نام خانوادگی',max_length=50,blank=True)
    seller_company= models.CharField('عنوان شرکت',max_length=50,blank=True)
    economic_id   = models.CharField('شماره اقتصادی',max_length=11)
    national_code = models.CharField('شماره/شناسه ملی',max_length=11)
    title       =   models.CharField('عنوان خرید',max_length=100,blank=True)
    year        =   models.IntegerField('سال',choices=YEAR_CHOICES)
    month       =   models.IntegerField('ماه',choices=MONTH_CHOICES)
    day         =   models.IntegerField('روز',choices=DAY_CHOICES)
    doc_number  =   models.CharField('شماره فاکتور',max_length=30)
    gross_amount=   models.DecimalField('مبلغ ناخالص',max_digits=20,decimal_places=2)
    VAT_included=   models.BooleanField('مالیات بر ارزش افزوده ',choices=TAX_STATUS, default=True)
    VAT_amount  =   models.DecimalField('مبلغ ارزش افزوده',max_digits=20,decimal_places=2)
    pay_amount  =   models.DecimalField('مبلغ پرداختی',max_digits=20,decimal_places=2,default=0)
    phone_number=   models.CharField("شماره تلفن",max_length=11)
    city_name   =   models.ForeignKey(City,verbose_name="شهر",null=True,on_delete=models.SET_NULL)
    address     =   models.TextField(verbose_name="آدرس",blank=True)
    description =   models.CharField(max_length=100,null=True,blank=True)

    class Meta:
        ordering=['year','month','day']

    def __str__(self):
        return "{}-{}-{}-{}".format(self.year,self.month,self.contract,self.gross_amount)
    

class Income(models.Model):
    YEAR_CHOICES=[
        (1396,'1396'),
        (1397,'1397'),
        (1398,'1398'),
        (1399,'1399'),
        (1400,'1400'),
    ]

    MONTH_CHOICES=[
        (1,'فروردین'),
        (2,'اردیبشت'),
        (3,'خرداد'),
        (3,'تیر'),
        (5,'مرداد'),
        (6,'شهریور'),
        (7,'مهر'),
        (8,'آبان'),
        (9,'آذر'),
        (10,'دی'),
        (11,'بهمن'),
        (12,'اسفند'),
    ]

    DAY_CHOICES=[
        (1,'1'),
        (2,'2'),
        (3,'3'),
        (4,'4'),
        (5,'5'),
        (6,'6'),
        (7,'7'),
        (8,'8'),
        (9,'9'),
        (10,'10'),
        (11,'11'),
        (12,'12'),
        (13,'13'),
        (14,'14'),
        (15,'15'),
        (16,'16'),
        (17,'17'),
        (18,'18'),
        (19,'19'),
        (20,'20'),
        (21,'21'),
        (22,'22'),
        (23,'23'),
        (24,'24'),
        (25,'25'),
        (26,'26'),
        (27,'27'),
        (28,'28'),
        (29,'29'),
        (30,'30'),
        (31,'31'),
    ]

    TAX_STATUS=[
        (True,'مشمول'),
        (False,'معاف')
    ]
    employeer   =   models.ForeignKey(Employeer,verbose_name='کارفرما',on_delete=models.CASCADE)
    contract    =   models.ForeignKey(Contract,verbose_name='قرارداد',max_length=150,on_delete=models.CASCADE)
    title       =   models.CharField('عنوان پرداخت',max_length=100,blank=True)
    year        =   models.IntegerField('سال',choices=YEAR_CHOICES)
    month       =   models.IntegerField('ماه',choices=MONTH_CHOICES)
    day         =   models.IntegerField('روز',choices=DAY_CHOICES)
    bank        =   models.ForeignKey(Bank,verbose_name='بانک',on_delete=models.CASCADE,null=True,blank=True,default='')
    doc_number  =   models.CharField('شماره سند',max_length=30)
    gross_amount=   models.DecimalField('مبلغ ناخالص',max_digits=20,decimal_places=2)
    VAT_included=   models.BooleanField('مالیات بر ارزش افزوده ',choices=TAX_STATUS, default=True)
    VAT_amount  =   models.DecimalField('مبلغ ارزش افزوده',max_digits=20,decimal_places=2)
    tax_included=   models.BooleanField('وضعیت مالیات تکلیفی',choices=TAX_STATUS, default=True,)
    tax_amount  =   models.DecimalField('مبلغ مالیات',max_digits=20,decimal_places=2)
    pay_amount  =   models.DecimalField('خالص پرداختی',max_digits=20,decimal_places=2,default=0)
    description =   models.CharField(max_length=100,null=True,blank=True)

    class Meta:
        ordering=['year','month','day']

    def __str__(self):
        return "{}-{}-{}-{}".format(self.year,self.month,self.contract,self.gross_amount)
    


