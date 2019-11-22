from django.db import models
from django.contrib.auth.models import User
import datetime
# Create your models here.
class Category(models.Model):
    title           = models.CharField("عنوان",max_length=60)

    def __str__(self):
        return self.title

class Documnet(models.Model):
    category        = models.ForeignKey(Category,verbose_name='عنوان گروه',on_delete=models.SET_NULL,null=True)
    title           = models.CharField("عنوان سند",max_length=60)
    doc_file        = models.FileField("فایل",upload_to='income/static/contracts/Documents')
    created_date    = models.DateField('تاریخ ایجاد',default=datetime.date.today())
    added_by_user   = models.ForeignKey(User ,verbose_name="کاربر ایجاد کننده",on_delete=models.SET_NULL,null=True)

    def __str__(self):
        return '{}-{}'.format(self.category,self.title)