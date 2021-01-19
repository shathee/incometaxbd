from django.db import models

# Create your models here.

class Zone(models.Model):
    name = models.CharField(max_length=50, blank=False, null=False, verbose_name='Zone Name')
    acc_code_company = models.CharField(max_length=20, blank=True, null=True)
    acc_code_except_company = models.CharField(max_length=20, blank=True, null=True)
    acc_code_other_fee = models.CharField(max_length=20, blank=True, null=True)
    phone = models.CharField(max_length=15, blank=True, null=True)
    address = models.TextField(max_length=50, blank=True, null=True)