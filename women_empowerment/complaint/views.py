from django.shortcuts import render
from complaint.models import Complaint
import datetime
# Create your views here.
def postcmp(request):
    if request.method=="POST":
        eid=str(request.session["u_id"])
        obj=Complaint()
        obj.complaint=request.POST.get('complaint')
        obj.date=datetime.date.today()
        obj.time=datetime.datetime.now().time()
        obj.pu_id=eid
        obj.reply=""
        obj.save()
    return render(request,'complaint/post complaint.html')
def viewcmp(request):
    objlist=Complaint.objects.all()
    context={
        'objval':objlist
    }

    return render(request,'complaint/view complaint.html',context)
def postreply(request,idd):
    objlist=Complaint.objects.filter(c_id=idd)
    context={
        'objval':objlist,
    }
    if request.method=="POST":
        obj=Complaint.objects.get(c_id=idd)
        obj.reply=request.POST.get('rep')
        obj.save()
    return render(request,'complaint/post reply.html',context)
def viewreply(request):
    objlist=Complaint.objects.all()
    context={
        'objval':objlist,
    }
    return render(request,'complaint/view reply.html',context)