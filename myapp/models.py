from django.db import models

class Users(models.Model):
    name = models.CharField(max_length=40)
    salary = models.DecimalField(max_digits=10, decimal_places=2)
    designation = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=15)
    company_name = models.CharField(max_length=15)
    department = models.CharField(max_length=100)
    role = models.CharField(max_length=100)
    gender = models.CharField(max_length=40)
    age = models.IntegerField()
    dob = models.DateField()
    
    def __str__(self):
        return self.name