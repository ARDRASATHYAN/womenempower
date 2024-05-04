from django.shortcuts import render
from public_user.models import PublicUser,Hire
from login.models import Login
from django.contrib import messages
import datetime
# Create your views here.
def reg(request):
    if request.method=="POST":
        obj=PublicUser()
        obj.name=request.POST.get('name')
        obj.address=request.POST.get('address')
        obj.gender=request.POST.get('gender')
        obj.qualification=request.POST.get('quali')
        obj.experience=request.POST.get('exp')
        obj.skill=request.POST.get('skill')
        obj.phone_number=request.POST.get('phone')
        obj.email=request.POST.get('em')
        obj.password=request.POST.get('pass')
        obj.save()
        ob=Login()
        ob.username=request.POST.get('em')
        ob.password=request.POST.get('pass')
        ob.type="public user"
        ob.u_id=obj.pu_id
        ob.save()
        objlist = "User Registered Successfully..  "
        context = {
            'msg': objlist
        }
        return render(request,'public_user/reg public user.html',context)
    return render(request,'public_user/reg public user.html')

def update(request):
    idd=str(request.session["u_id"])
    obj=PublicUser.objects.filter(pu_id=idd)
    context={
        'objval':obj,
    }
    if request.method=="POST":
        obj=PublicUser.objects.get(pu_id=idd)
        obj.name = request.POST.get('name')
        obj.address = request.POST.get('address')
        obj.gender = request.POST.get('gender')
        obj.qualification = request.POST.get('quali')
        obj.experience = request.POST.get('exp')
        obj.skill = request.POST.get('skill')
        obj.phone_number = request.POST.get('phone')
        obj.email = request.POST.get('em')
        obj.password = request.POST.get('pass')
        obj.save()
        messages.info(request, 'Updated successfully!')

    return render(request,'public_user/update profile.html',context)
def hire(request):
    if request.method=="POST":
        eid=str(request.session["u_id"])
        uid=str(request.session["u_id"])
        obj=Hire()
        obj.job_details=request.POST.get('jd')
        obj.r_id=eid
        obj.pu_id=uid
        obj.date=datetime.date.today()
        obj.status="pending"
        obj.save()

    return render(request,'public_user/hire.html')
def labour(request):
    objlist=PublicUser.objects.all()
    context={
        'objval':objlist,
    }
    return render(request,'public_user/hire labour.html',context)
def manage(request):
    objlist = Hire.objects.all()
    context = {
        'objval': objlist,
    }
    return render(request,'public_user/manage hired notification.html',context)
def papprove(request,idd):
    obj=Hire.objects.get(h_id=idd)
    obj.status="approved"
    obj.save()
    return manage(request)
def preject(request,idd):
    obj=Hire.objects.get(h_id=idd)
    obj.status="rejected"
    obj.save()
    return manage(request)