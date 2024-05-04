from django.shortcuts import render
from sales_report.models import SalesReport
# Create your views here.
def report(request):
    objlist = SalesReport.objects.all()
    context = {
        'objval': objlist,
    }
    return render(request,'sales_report/view sales report.html',context)
def salereport(request):
    objlist = SalesReport.objects.all()
    context = {
        'objval': objlist,
    }
    return render(request,'sales_report/viewsalesr.html',context)