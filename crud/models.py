from django.db import models

# Create your models here.
class Detail(models.Model):
    accname=models.CharField(max_length=90)
    age=models.IntegerField()
    password=models.CharField(max_length=200)

    def __str__ (self):
        return f'accname{self.accname}'