# from django.db import models

# Create your models here.
from django.db import models

class EmployeeEmails(models.Model):
    query_id = models.IntegerField(default=0, blank=True)
    table1 = models.CharField(max_length=300,null=True,blank=True)

    def __str__(self):
        return self.query_id