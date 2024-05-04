from django.db import models

# Create your models here.
class Sell(models.Model):
    se_id = models.AutoField(primary_key=True)
    r_id = models.IntegerField()
    username = models.CharField(max_length=20)
    product = models.CharField(max_length=40)
    quantity = models.CharField(max_length=30)
    price = models.CharField(max_length=30)
    image = models.CharField(max_length=50)
    status = models.CharField(max_length=30)

    class Meta:
        managed = False
        db_table = 'sell'


