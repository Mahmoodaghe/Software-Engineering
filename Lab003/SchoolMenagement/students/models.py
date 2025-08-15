from django.db import models

# Create your models here.

class student(models.Model):
    Levels=[('1','1'),('2','2'),('3','3'),('4','4')]
    F_name=models.CharField(max_length=10,default="Student")
    L_name=models.CharField(max_length=10,default="Student")
    age=models.IntegerField()
    level=models.CharField(choices=Levels,max_length=20)
    gpa=models.IntegerField()
    statust=models.BooleanField(null=False)
    report=models.TextField(max_length=300)
    def __str__(self):
        return f"{self.F_name}{self.L_name}"