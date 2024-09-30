# myapp/models.py

from django.db import models

class PersonData(models.Model):
    name = models.CharField(max_length=100)
    fathers_name = models.CharField(max_length=100)
    mothers_name = models.CharField(max_length=100)
    address = models.TextField()
    NID = models.IntegerField()
    dob = models.DateField()
    blood_group = models.CharField(max_length=3)

    def __str__(self):
        return self.name
