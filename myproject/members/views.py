# members/views.py
from django.shortcuts import render
from .models import Role, Project, ContactInfo, About, Skill

def home(request):
    roles = Role.objects.all()
    about = About.objects.all()
    skill = Skill.objects.all()
    project = Project.objects.all()
    contact = ContactInfo.objects.first()


    context = {
        'name': 'Sumit Ray',
        'roles': roles,
        'about': about,
        'skill': skill,
        'project': project,
        'contact': contact,
    }

    return render(request, 'index.html', context)
