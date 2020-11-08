from django.db import models
from django.contrib.auth.models import User


# Create your models here.



class Outsourcing(models.Model):
    BUDGET_CHOICE=(
        ('smallproject','smallproject'),
        ('mediumproject','mediumproject'),
        ('largeproject','largeproject'),
    )

    PAY_CHOICE=(
        ('fixed','fixed'),
        ('hourly','hourly'),
    )

    title=models.CharField(max_length=100)
    description=models.CharField(max_length=300)
    upload=models.FileField(upload_to='media/date/%Y/%M/%D/')
    skills=models.CharField(max_length=100)
 
    budget=models.CharField(max_length=100,choices=BUDGET_CHOICE)
    payment=models.CharField(max_length=100,choices=PAY_CHOICE)
    bids=models.BooleanField(default=False)
    time_reqd=models.CharField(max_length=100)
