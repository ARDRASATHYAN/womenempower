from django.db import models

# Create your models here.
class Payment(models.Model):
    pay_id = models.AutoField(primary_key=True)
    pu_id = models.IntegerField()
    bank_name = models.CharField(max_length=50)
    account_number = models.CharField(max_length=40)
    payment_type = models.CharField(max_length=30)
    total_amount = models.IntegerField()
    ifsc_code = models.CharField(max_length=30)

    class Meta:
        managed = False
        db_table = 'payment'


