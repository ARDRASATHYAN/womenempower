from django.shortcuts import render
from order.models import Order
from product.models import Product
import datetime
# Create your views here.
def order(request,idd):
    objlist=Product.objects.get(p_id=idd)
    context={
        'objval':objlist
    }
    if request.method=="POST":
        eid=str(request.session["u_id"])
        obj=Order()
        obj.pu_id=eid
        obj.p_id=1
        obj.quantity=request.POST.get('qty')
        obj.order_date=datetime.date.today()
        obj.status="pending"
        obj.save()
    return render(request,'order/order product.html',context)
def vieworder(request):
    objlist = Order.objects.filter(status=forwarded)
    context = {
        'objval': objlist,
    }
    return render(request,'order/view order.html',context)
def manage(request):
    objlist = Order.objects.filter(status='pending')
    context = {
        'objval': objlist,
    }

    return render(request,'order/manage order.html',context)
def forwarded(request,idd):
    obj = Order.objects.get(o_id=idd)
    obj.status = "Forwarded"
    obj.save()
    return manage(request)
    # return render(request,'order/manage order.html',context)

def accept(request,idd):
    obj=Order.objects.get(o_id=idd)
    obj.status="Accepted"
    obj.save()
    return manage(request)
def cancell(request,idd):
    obj=Order.objects.get(o_id=idd)
    obj.status="Cancelled"
    obj.save()
    return manage(request)