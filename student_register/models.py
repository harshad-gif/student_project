from django.db import models

# Create your models here.

class Branch(models.Model):
    title = models.CharField(max_length=30)

    def __str__(self):
        return self.title

class Student(models.Model):
    fullname = models.CharField(max_length=50)
    mobile = models.CharField(max_length=20)
    stu_Code = models.CharField(max_length=5)
    branch = models.ForeignKey(Branch,on_delete=models.CASCADE)