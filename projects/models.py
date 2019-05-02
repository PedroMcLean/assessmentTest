from django.db import models

#Class and variable declarations
class Project(models.Model):
    projectName = models.CharField(max_length=50)
    projectStatus = models.CharField(max_length=50)

    def __str__(self):
        return self.projectName
