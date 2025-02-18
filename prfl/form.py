
from django import forms
from .models import Certificate, Profile, Education, Project,  WorkExperience
from django.contrib.auth.models import User


class ProfileForm(forms.ModelForm):
    username = forms.CharField(max_length=150, required=True)  
    email = forms.EmailField(required=True)  

    class Meta:
        model = Profile
        fields = ["username", "email", "bio", "location", "profile_pics"]
    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user', None)
        super().__init__(*args, **kwargs)

        if user:
            self.fields["username"].initial = user.username
            self.fields["email"].initial = user.email

    def save(self, user=None, commit=True):
        profile = super().save(commit=False)  # Don't save yet

        if user:
            profile.user = user
            user.username = self.cleaned_data["username"]
            user.email = self.cleaned_data["email"]
            user.save()  # ✅ Save User details

        if commit:  
            profile.save()  # ✅ Ensure profile gets saved
            self.save_m2m()  # Save many-to-many relationships if any
        return profile

    
class EducationForm(forms.ModelForm):
    class Meta:
        model = Education
        fields = ["institution", "degree", "start_date", "end_date"]

class CertificateForm(forms.ModelForm):
    class Meta:
        model = Certificate
        fields = ['name', 'issuing_organization', 'issue_date']

class WorkExperienceForm(forms.ModelForm):
    class Meta:
        model = WorkExperience
        fields = ["company_name", "role", "start_date", "end_date", "description"]

class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = ["title", "description", "project_image", "project_link"]