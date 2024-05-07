from django.db import models

# Create your models here.
class Dept(models.Model):
    deptno=models.IntegerField(primary_key=True)
    dname=models.CharField(max_length=100,unique=True)
    dloc=models.CharField(max_length=100)
    def __str__(self):
        return str(self.deptno)
    
    
class Emp(models.Model):
    empno=models.IntegerField(primary_key=True)
    ename=models.CharField(max_length=100)
    job=models.CharField(max_length=100)
    Sal=models.DecimalField(max_digits=10,decimal_places=2)
    Mgr=models.ForeignKey('self',on_delete=models.SET_NULL,null=True,blank=True)
    Comm=models.DecimalField(max_digits=10,decimal_places=2)
    Hiredate=models.DateField()
    Deptno=models.ForeignKey(Dept,on_delete=models.CASCADE)

    def __str__(self):
        return self.ename


class Salgrade(models.Model):
    Grade=models.IntegerField(primary_key=True)
    losal=models.DecimalField(max_digits=10,decimal_places=2)
    highsal=models.DecimalField(max_digits=10,decimal_places=2)

    def __str__(self):
        return str(self.Grade)

