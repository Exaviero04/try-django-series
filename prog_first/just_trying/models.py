from django.db import models

# Create your models here.
class product(models.Model):
    description = models.TextField(default="yo")
    title = models.CharField(max_length=75)

class random(models.Model):
    ran=models.TimeField()
    why=models.DecimalField(decimal_places=7,max_digits=200,blank=True,null=True)
