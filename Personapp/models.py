from django.db import models
from django.db.models import CASCADE

# Create your models here.



class Department(models.Model):
    dep_name = models.CharField(max_length=210,unique=True)


    def __str__(self):
      return self.dep_name
    

class Course(models.Model):
   course_name = models.CharField(max_length=210,unique=True)
   department = models.ForeignKey(Department,on_delete=models.CASCADE)

   def __str__(self):
     return self.course_name


class Gender(models.Model):
    gender_name = models.CharField(max_length=100,unique=True)

    def __str__(self):
     return self.gender_name    


class Purpose(models.Model):
    purpose_name = models.CharField(max_length=100,unique=True)

    def __str__(self):
     return self.purpose_name    


# class Material(models.Model):
#    material_name = models.TextField(max_length=100,default=True)


class Person_profile(models.Model):
    name = models.CharField(max_length=300,unique=True)
    dob = models.DateField(auto_now=False, auto_now_add=False)
    age = models.IntegerField(blank=True)
    gender = models.ForeignKey(Gender,on_delete=models.SET_NULL, blank=True, null=True)
    phone_number = models.IntegerField(blank=True)
    email = models.EmailField()
    address = models.TextField()
    department = models.ForeignKey(Department,on_delete=models.SET_NULL, blank=True, null=True)
    course = models.ForeignKey(Course,on_delete=models.SET_NULL, blank=True, null=True)
    purpose = models.ForeignKey(Purpose,on_delete=models.SET_NULL, blank=True, null=True)
    material = models.CharField(max_length=50)
    

def __str__(self):
    return self.name
