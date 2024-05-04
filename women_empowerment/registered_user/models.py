from django.db import models

# Create your models here.
class RegisteredUser(models.Model):
    r_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=30)
    address = models.CharField(max_length=50)
    gender = models.CharField(max_length=40)
    phone_number = models.CharField(max_length=30)
    catogory = models.CharField(max_length=30)
    email = models.CharField(max_length=50)
    status = models.CharField(max_length=30)

    class Meta:
        managed = False
        db_table = 'registered_user'



