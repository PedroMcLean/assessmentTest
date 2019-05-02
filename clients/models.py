from django.db import models

#Class and variable declarations
class Client(models.Model):
    clientName = models.CharField(max_length=50)
    contactPerson = models.CharField(max_length=50)
    contactNumber = models.CharField(max_length=20)

    def __str__(self):
        return self.clientName
