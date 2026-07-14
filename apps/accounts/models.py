from django.db import models
import uuid

#one to many relations
class Department(models.Model):
    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False
    )
    name = models.CharField(
        max_length=100,
        unique=True
    )
    created_at = models.DateTimeField(auto_now_add=True)



class Project(models.Model):
    id = models.UUIDField(primary_key=True,default=uuid.uuid4,editable=False)
    name = models.CharField(max_length=100)
    employees = models.ManyToManyField('Employee',through='Project_enrollment',related_name='projects')

class Employee(models.Model):
    id = models.UUIDField(primary_key=True,default=uuid.uuid4,editable=False)
    name = models.CharField(max_length=100)

    
class Project_enrollment(models.Model):
    employee = models.ForeignKey(Employee,on_delete=models.CASCADE,related_name='enrollments')
    project  = models.ForeignKey(Project,on_delete=models.CASCADE,related_name='enrollments')




