from django.shortcuts import render
from sell.models import Sell
from order.models import Order
from django.core.files.storage import FileSystemStorage

# Create your views here.
def sell(request):
    objlist=Order.objects.filter(status='forwarded')
    context={
        'objval':objlist,
    }
    return render(request,'sell/sell.html',context)
def remove(request,idd):
    obj=Sell.objects.get(se_id=idd)
    obj.status="cancell"
    obj.save()
    return sell(request)
# def psell(request,idd):
#     obj=Sell.objects.get(se_id=idd)
#     obj.status="delivery"
#     obj.save()
#     return sell(request)
def productsell(request,idd):
    ob=Order.objects.get(o_id=idd)
    ob1 = Order.objects.filter(o_id=idd)
    context={
        'objval':ob1,
    }
    if request.method=="POST" and 'sub' in request.POST:
        obj=Sell()
        obj.username=request.POST.get('un')
        obj.product=request.POST.get('product')
        obj.quantity=request.POST.get('quantity')
        obj.price=request.POST.get('price')
        # file=request.FILES['image']
        # ff=FileSystemStorage()
        # filename=ff.save(file.name,file)
        # obj.image=file.name
        # print(obj.image)
        # myfile=request.FILES['image']
        # fs=FileSystemStorage()
        # filename=fs.save(myfile.name,myfile)
        # image=myfile.name
        obj.image=ob.p.image
        # # print(obj.image)
        obj.r_id="3"
        obj.status="sell"
        obj.save()

        return sell(request)
    elif 'reject' in request.POST:
        obj = Order()
        obj.o_id=idd

        obj.delete()
        return sell(request)


    return render(request,'sell/sell product.html',context)