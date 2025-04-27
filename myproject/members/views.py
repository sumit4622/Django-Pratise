# members/views.py
from django.shortcuts import render
from .models import Role, Project, ContactInfo

def home(request):
    roles = Role.objects.all()
    project = Project.objects.all()
    contact = ContactInfo.objects.first()


    context = {
        'name': 'Sumit Ray',
        'roles': roles,
        'project': project,
        'contact': contact,
    }

    return render(request, 'index.html', context)
