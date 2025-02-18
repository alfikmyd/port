
from django.db import models
from django.contrib.auth.models import User

# Profile Model
# class Profile(models.Model):
#     user = models.OneToOneField(User, on_delete=models.CASCADE, unique=True)
#     bio = models.TextField(blank=True, null=True)
#     profile_picture = models.ImageField(upload_to="profile_pics/", blank=True, null=True)

#     email = models.EmailField()
#     location = models.CharField(max_length=100)
#     # profile_pics = models.ImageField(upload_to='profile_pics/', null=True, blank=True)
#     def __str__(self):
#         return self.user.username
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)  # Ensure one profile per user
    bio = models.TextField(blank=True, null=True)
    location = models.CharField(max_length=255, blank=True, null=True)
    profile_pics = models.ImageField(upload_to="profile_pics/", blank=True, null=True)

    def __str__(self):
        return self.user.username 

class Education(models.Model):
    institution = models.CharField(max_length=255)
    degree = models.CharField(max_length=255)
    start_date = models.DateField()
    end_date = models.DateField(null=True, blank=True)

    def __str__(self):
        return self.institution


class Certificate(models.Model):
    name = models.CharField(max_length=255)
    issuing_organization = models.CharField(max_length=255)
    issue_date = models.DateField()

    def __str__(self):
        return self.name
    

class WorkExperience(models.Model):
    company_name = models.CharField(max_length=255)
    role = models.CharField(max_length=255)
    start_date = models.DateField()
    end_date = models.DateField(null=True, blank=True)
    description = models.TextField(default="No description provided")
    

class Project(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    project_image = models.ImageField(upload_to='projects/', blank=True, null=True)
    project_link = models.URLField(max_length=500, blank=True, null=True)

    def __str__(self):
        return self.title