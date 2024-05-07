from django.shortcuts import render
from django.db.models import Q
from django.db.models.functions import Length

# Create your views here.
from app.models import *
def innerEquijoins(request):
    JDED=Emp.objects.select_related('Deptno').all()
    JDED=Emp.objects.select_related('Deptno').filter(job='Analyst')
    JDED=Emp.objects.select_related('Deptno').filter(Deptno__dloc='Chicago')
    JDED=Emp.objects.select_related('Deptno').filter(Deptno__dloc='Dallas')
    JDED=Emp.objects.select_related('Deptno').filter(Q(Deptno__dloc='Dallas') | Q(Deptno__dname='research'))
    JDED=Emp.objects.select_related('Deptno').filter(Hiredate='2024-04-22')
    JDED=Emp.objects.select_related('Deptno').filter(Sal__gt='25000')
    JDED=Emp.objects.select_related('Deptno').filter(ename__startswith='k')
    JDED=Emp.objects.select_related('Deptno').filter(Q(Deptno__dloc='Dallas') | Q(ename='aswini'))
    JDED=Emp.objects.select_related('Deptno').filter(ename__endswith='a')
    JDED=Emp.objects.select_related('Deptno').filter(Q(ename__startswith='k')| Q(Hiredate='2024-04-22'))
    JDED=Emp.objects.select_related('Deptno').filter(ename__contains='a')
    JDED=Emp.objects.select_related('Deptno').filter(Mgr=None)
    JDED=Emp.objects.select_related('Deptno').filter(Comm__gt=50)
    JDED=Emp.objects.select_related('Deptno').filter(Q(Sal__lt=30000)| Q(Hiredate='2024-04-15'))
    JDED=Emp.objects.select_related('Deptno').filter(Q(ename='priya') | Q(job='Analyst') | Q(empno=1368))
    d={'JDED':JDED}
    return render(request,'innerEquijoins.html',d)
