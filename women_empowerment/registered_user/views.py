from django.shortcuts import render
from registered_user.models import RegisteredUser
from login.models import Login
# Create your views here.
def reg(request):
    if request.method=="POST":
        obj=RegisteredUser()
        obj.name=request.POST.get('nm')
        obj.address=request.POST.get('adr')
        obj.gender=request.POST.get('gen')
        obj.phone_number=request.POST.get('ph')
        obj.catogory=request.POST.get('CATEGORY')
        obj.email=request.POST.get('em')
        obj.status="pending"
        obj.save()
        ob=Login()
        ob.username=request.POST.get('em')
        ob.password=request.POST.get('pass')
        ob.type="registered user"
        ob.u_id=obj.r_id
        ob.save()
    return render(request,'registered_user/register ru.html')
def manage(request):
    objlist = RegisteredUser.objects.all()
    context = {
        'objval': objlist,
    }
    return render(request,'registered_user/manage ruser.html',context)
def approve(request,idd):
    obj=RegisteredUser.objects.get(r_id=idd)
    obj.status="approved"
    obj.save()
    return manage(request)
def reject(request,idd):
    obj=RegisteredUser.objects.get(r_id=idd)
    obj.status="rejected"
    obj.save()
    return manage(request)
