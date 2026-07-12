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
    name = models.CharField(max_length=100)

class Employee(models.Model):
    id = models.UUIDField(primary_key=True,default=uuid.uuid4,editable=False)
    name = models.CharField(max_length=100)
    department = models.ForeignKey(Department,on_delete=models.PROTECT,related_name="employees")
    projects = models.ManyToManyField(Project,related_name='employees')
#many to many rel




