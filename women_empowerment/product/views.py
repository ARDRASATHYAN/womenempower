from django.shortcuts import render
from product.models import Product
from django.core.files.storage import FileSystemStorage
# Create your views here.
def product(request):
    if request.method=="POST":
        eid=str(request.session["u_id"])
        obj=Product()
        obj.product_name=request.POST.get('pn')
        obj.product_code=request.POST.get('pc')
        obj.description=request.POST.get('des')
        obj.type=request.POST.get('type')
        obj.stock=request.POST.get('stock')
        # obj.image=request.POST.get('image')
        obj.price=request.POST.get('price')
        obj.r_id=eid
        myfile = request.FILES['image']
        fs = FileSystemStorage()
        filename = fs.save(myfile.name, myfile)
        obj.image = myfile.name
        obj.status = 'pending'

        obj.save()
    return render(request,'product/register product.html')
def manage(request):
    objlist = Product.objects.all()
    context = {
        'objval': objlist,
    }
    return render(request,'product/manage product.html',context)
def search(request):
    ob = Product.objects.all()
    context = {
        'objval': ob,
    }
    if request.method=="POST":
        search=request.POST.get('nm')
        ob=Product.objects.filter(product_name__icontains=search)
        context={
            'objval':ob,
        }
        return render(request,'product/search product.html',context)
    return render(request,'product/search product.html',context)
def aapprove(request,idd):
    obj=Product.objects.get(p_id=idd)
    obj.status="approved"
    obj.save()
    return manage(request)
def areject(request,idd):
    obj=Product.objects.get(p_id=idd)
    obj.status="rejected"
    obj.save()
    return manage(request)