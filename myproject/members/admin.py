from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Role, Project, ContactInfo,About,Skill

admin.site.register(Role)
admin.site.register(About)
admin.site.register(Skill)
admin.site.register(Project)
admin.site.register(ContactInfo)
