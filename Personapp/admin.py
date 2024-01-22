from django.contrib import admin
from .models import Department,Course,Person_profile,Gender,Purpose

# Register your models here.

admin.site.register(Department)
admin.site.register(Course)
admin.site.register(Person_profile)
admin.site.register(Gender)
admin.site.register(Purpose)
# admin.site.register(Material)
