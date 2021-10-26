from django.db import models

class Cost(models.Model):

    cost_title = models.CharField(max_length=30, verbose_name= "شرح هزینه")
    cost_type = models.CharField(max_length=100, verbose_name= "نوع هزینه")
    cost_date = models.DateField(verbose_name= "تاریخ ")
    cost_amount = models.IntegerField(verbose_name= "مبلغ هزینه")
    cost_description = models.TextField(max_length=300,verbose_name= "توضیحات هزینه")
