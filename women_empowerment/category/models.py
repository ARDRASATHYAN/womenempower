from django.db import models

# Create your models here.
class Category(models.Model):
    ca_id = models.AutoField(primary_key=True)
    category = models.CharField(max_length=30)

    class Meta:
        managed = False
        db_table = 'category'

