# from django.db import models
#
# class Student(models.Model):
#     name=models.CharField(max_length=100)
#     roll= models.IntegerField()
#     city= models.CharField(max_length=100)
#
#     def __str__(self):
#         return self.title

from django.db import models

class Book(models.Model):
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    price=models.IntegerField
    published_date = models.DateField()
    image=models.ImageField(upload_to='images/',max_length=255,null=True,blank=True)
    PDF=models.FileField(upload_to='pdfs/',null=True,blank=True)


    def __str__(self):
        return self.title