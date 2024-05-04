from django.shortcuts import render
from delivery.models import Delivery
from delivery.models import Sell
import datetime
# Create your views here.
def assign(request):
    objlist=Sell.objects.filter(status='sell')
    context={
        'objval':objlist,
    }

    return render(request,'delivery/assign delivery.html',context)
def view(request):
    objlist=Delivery.objects.all()
    context={
        'objval':objlist,
    }
    return render(request,'delivery/view delivery status.html',context)

def delivery(request,idd):
    obj=Sell.objects.filter(se_id=idd)
    context={
        'val':obj,
    }
    if request.method == "POST":
        eid=str(request.session["u_id"] )
        obj = Sell.objects.get(se_id=idd)
        obj.status = "deliverd"
        obj.se_id=idd
        obj.save()

        ob = Delivery()
        ob.product_name=request.POST.get('pn')
        ob.quantity=request.POST.get('qty')
        ob.order_date=datetime.date.today()
        ob.pu_id=eid
        ob.status = "sell"
        ob.amount=obj.price
        ob.save()
        return assign(request)
    return render(request, 'delivery/view delivery.html',context)

    # if request.method=="POST":
    #     obj=Delivery()
    #     obj.status=delivery

