from django.db import models

# Create your models here.
class PublicUser(models.Model):
    pu_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=30)
    address = models.CharField(max_length=50)
    gender = models.CharField(max_length=40)
    qualification = models.CharField(max_length=30)
    experience = models.CharField(max_length=30)
    skill = models.CharField(max_length=50)
    phone_number = models.CharField(max_length=30)
    email = models.CharField(max_length=40)
    password = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'public_user'
class Hire(models.Model):
    h_id = models.AutoField(primary_key=True)
    r_id = models.IntegerField()
    pu_id = models.IntegerField()
    job_details = models.CharField(max_length=50)
    date = models.DateField()
    status = models.CharField(max_length=30)

    class Meta:
        managed = False
        db_table = 'hire'

