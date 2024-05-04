from django.db import models
from product.models import Product
# Create your models here.
class Rating(models.Model):
    rate_id = models.AutoField(primary_key=True)
    pu_id = models.IntegerField()
    # p_id = models.IntegerField()
    p = models.ForeignKey(Product, to_field='p_id', on_delete=models.CASCADE)
    rating = models.CharField(max_length=30)

    class Meta:
        managed = False
        db_table = 'rating'
