from django.db import models
from django.core.exceptions import ValidationError
import re


DC = [
    ('HR', 'Human Resources'),
    ('IT', 'Information Technology'),
    ('FIN', 'Finance'),
    ('MKT', 'Marketing'),
    ('OPS', 'Operations'),
    ('SALES', 'Sales'),
]


class Employee(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=15)
    salary = models.DecimalField(max_digits=10, decimal_places=2)
    date_of_joining = models.DateField()
    department = models.CharField(max_length=15, choices=DC)
    profile_picture = models.ImageField(upload_to='employee_images/', null=True, blank=True)
    resume = models.FileField(upload_to='employee_resumes/', null=True, blank=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name} ({self.email})"
    
    def clean(self):
        if not re.match(r"[^@]+@[^@]+\.[^@]+", self.email):
            raise ValidationError("Invalid email format.")
        
        if not self.email.lower().endswith("@company.com"):
            raise ValidationError("Email must be a company email (e.g., user@company.com).")
        

    


