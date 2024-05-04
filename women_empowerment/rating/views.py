from django.shortcuts import render
from rating.models import Rating
from product.models import Product
# Create your views here.
def rating(request):
    ob=Product.objects.all()
    context={
        'val':ob,
    }
    if request.method=="POST":
        eid=str(request.session["u_id"] )
        obj=Rating()
        obj.rating=request.POST.get('rating')
        obj.p_id=request.POST.get('p')
        obj.pu_id=eid
        obj.save()

    return render(request,'rating/rating.html',context)
def viewrating(request):
    objlist=Rating.objects.all()
    context={
        'objval':objlist,
    }
    return render(request,'rating/view rating.html',context)
def viewpr(request):
    objlist = Rating.objects.all()
    context = {
        'objval': objlist,
    }
    return render(request,'rating/view product rating.html',context)
