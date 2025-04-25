from django.shortcuts import render
from .models import Project, ContactInfo

def home(request):
    # Fallback data, with the same keys as the DB dicts
    raw_fallback = [
        {
            'title': 'Portfolio Website',
            'desc': 'A personal portfolio built using Django and React',
            'image_url': '/static/Image/placeholder.png',
            'link': '#'
        },
        {
            'title': 'E-commerce Site',
            'desc': 'An online store with payment gateway integration',
            'image_url': '/static/Image/placeholder.png',
            'link': '#'
        }
    ]

    db_qs = Project.objects.all()
    if db_qs.exists():
        projects = [
            {
                'title': p.title,
                'desc':  p.desc,
                'image_url': p.image.url,
                'link':   p.link
            }
            for p in db_qs
        ]
    else:
        projects = raw_fallback

    contact = ContactInfo.objects.first()  # assumes you have at least one

    context = {
        'name': 'Sumit Ray',
        'projects': projects,
        'contact': contact,
    }
    return render(request, 'index.html', context)
