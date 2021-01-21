from django.db import models

# Create your models here.

class Profile(models.Model):
    name = models.CharField(max_length=50, blank=False, null=False, verbose_name='Name of the Assessee')
    mothers_name =  models.CharField(max_length=50, blank=True, null=True)
    fathers_name =  models.CharField(max_length=50, blank=True, null=True)
    spouse_name =  models.CharField(max_length=50, blank=True, null=True)
    email = models.EmailField(blank=False, null=False)
    mobile = models.CharField(max_length=15, blank=True, null=True)
    profile_type = models.CharField(max_length=2, choices=[('F', 'Farmer'), ('S', 'SaAEO')], default='F')
    gender = models.CharField(max_length=2, choices=[('M', 'Male'), ('F', 'Female')], default='M')
    twelve_digit_TIN =  models.CharField(max_length=15, blank=False, null=False, default='00')
    old_TIN =  models.CharField(max_length=16, blank=False, null=False, default='00')
    # tax_circle = 
    # tax_circle = 
    
    def __str__(self):
        return 'Profile: {}'.format(self.name)