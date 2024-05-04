from django.db import models

# Create your models here.
class SalesReport(models.Model):
    s_id = models.AutoField(primary_key=True)
    product_name = models.CharField(max_length=30)
    price = models.CharField(max_length=50)
    report = models.CharField(max_length=40)

    class Meta:
        managed = False
        db_table = 'sales_report'

