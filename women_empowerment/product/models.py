from django.db import models

# Create your models here.
class Product(models.Model):
    p_id = models.AutoField(primary_key=True)
    r_id = models.IntegerField()
    product_name = models.CharField(max_length=50)
    product_code = models.CharField(max_length=40)
    description = models.CharField(max_length=50)
    type = models.CharField(max_length=30)
    price = models.CharField(max_length=30)
    stock = models.CharField(max_length=30)
    image = models.CharField(max_length=100)
    status = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'product'

