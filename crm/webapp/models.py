from django.db import models

class Record(models.Model):

    Creation_date = models.DateTimeField(auto_now_add=True)

    First_name = models.CharField(max_length=100)

    Last_name = models.CharField(max_length=100)

    Email = models.CharField(max_length=150)

    Phone = models.CharField(max_length=20)

    Address = models.CharField(max_length=300)

    Company = models.CharField(max_length=255)

    def __str__(self):

        return self.First_name + " " + self.Last_name




