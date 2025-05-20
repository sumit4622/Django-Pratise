from django.shortcuts import render, redirect
from .forms import ContactForm
from .models import Role, Project, ContactInfo, About, Skill

def home(request):
    roles = Role.objects.all()
    about = About.objects.all()
    skill = Skill.objects.all()
    project = Project.objects.all()
    contact = ContactInfo.objects.first()

    # Handle contact form submission
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')  # Redirect to clear POST
    else:
        form = ContactForm()

    context = {
        'name': 'Sumit Ray',
        'roles': roles,
        'about': about,
        'skill': skill,
        'project': project,
        'contact': contact,
        'form': form,  
    }

    return render(request, 'index.html', context)
