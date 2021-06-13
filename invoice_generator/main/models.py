from django.db import models

# Create your models here.

class Invoices(models.Model):
    
    invoice_id=models.IntegerField(unique=True)
    details=models.TextField()
    

    
    
    
    