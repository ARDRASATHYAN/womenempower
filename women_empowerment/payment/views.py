from django.shortcuts import render
from payment.models import Payment
# Create your views here.
def payment(request):
    if request.method=="POST":
        eid=str(request.session["u_id"])
        obj=Payment()
        obj.pu_id=eid
        obj.bank_name=request.POST.get('bn')
        obj.account_number=request.POST.get('ban')
        obj.total_amount=request.POST.get('ta')
        obj.payment_type=request.POST.get('payment')
        obj.ifsc_code=request.POST.get('code')
        obj.save()
    return render(request,'payment/payment.html')
def viewpay(request):
    objlist = Payment.objects.all()
    context = {
        'objval': objlist,
    }
    return render(request,'payment/view payment.html',context)