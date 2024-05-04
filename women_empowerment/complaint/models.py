from django.db import models

# Create your models here.
class Complaint(models.Model):
    c_id = models.AutoField(primary_key=True)
    pu_id = models.IntegerField()
    complaint = models.CharField(max_length=50)
    date = models.DateField()
    time = models.TimeField()
    reply = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'complaint'

