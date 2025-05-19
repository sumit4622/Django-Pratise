from django.db import models

# Create your models here.
from django.db import models

class Role(models.Model):
    heading = models.CharField(max_length=100, null=True, blank=True)
    title = models.CharField(max_length=100)
    progress = models.IntegerField()

    def __str__(self):
        return self.title

class About(models.Model):
    name = models.CharField(max_length=100, null= True, blank=True)
    paragraph = models.CharField(max_length=650, null= True, blank=True)
    paragraph1 = models.CharField(max_length=940, null=True, blank=True)
    

    def __str__(self):
        return "About"

class Skill(models.Model):
    skillName = models.CharField(max_length=50, null=True, blank=True)
    skillpercent = models.CharField(max_length=50, null=True, blank=True)

    def __str__(self):
        return "Skill"

class Project(models.Model):
    title = models.CharField(max_length=200)
    desc = models.TextField()
    image = models.ImageField(upload_to='project_images/')
    link = models.URLField(blank=True)

    def __str__(self):
        return "Project"

class ContactInfo(models.Model):
    location = models.CharField(max_length=200)
    phone = models.CharField(max_length=20)
    email = models.EmailField()

    def __str__(self):
        return "Contact Info"
