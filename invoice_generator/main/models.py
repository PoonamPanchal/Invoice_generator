from django.db import models

# Create your models here.

class Invoices(models.Model):
    
    invoice_id=models.IntegerField(max_length=5,unique=True)
    details=models.TextField()
    

    
    
    
    