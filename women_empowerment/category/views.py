from django.shortcuts import render
from category.models import Category
# Create your views here.
def category(request):
    if request.method=="POST":
        obj=Category()
        obj.category=request.POST.get('ct')
        obj.save()
    return render(request,'category/catogory.html')