from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User
from django.utils import timezone
import datetime
# Create your models here.
class Category(models.Model):
    title           = models.CharField("عنوان",max_length=60)

    def __str__(self):
        return self.title

class Documnet(models.Model):
    category        = models.ForeignKey(Category,verbose_name='عنوان گروه',on_delete=models.SET_NULL,null=True)
    title           = models.CharField("عنوان سند",max_length=60)
    doc_file        = models.ImageField("فایل",upload_to='photos/')
    created_date    = models.DateField('تاریخ ایجاد')
    added_by_user   = models.ForeignKey(User ,verbose_name="کاربر ایجاد کننده",on_delete=models.SET_NULL,null=True)

    def __str__(self):
        return '{}-{}'.format(self.category,self.title)

    def get_absolute_url(self):
        return reverse('document-detail',kwargs={'pk':self.id})