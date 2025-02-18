
from django.shortcuts import get_object_or_404, redirect, render
from .models import Profile,WorkExperience,Education,Project,Certificate
from django.contrib.auth.models import User
from .form import CertificateForm,ProfileForm,EducationForm,ProjectForm,WorkExperienceForm

# def createProfile(request):
#     if request.method == "POST":
#         form = ProfileForm(request.POST, request.FILES)
#         username = request.POST.get("username")
#         if form.is_valid():
#             user_profile, created = Profile.objects.get_or_create(user=request.user)
#             if not created:  # Profile already exists
#                 return redirect("profile")  # Redirect instead of creating duplicate

#             user_profile.bio = form.cleaned_data["bio"]
#             user_profile.profile_pics = form.cleaned_data["profile_pics"]
            
#             user_profile.save()

#             return redirect("profile_list.html")

#     else:
#         form = ProfileForm()

#     return render(request, "profile.html", {"form": form})
def createProfile(request):
    if request.method == "POST":
        profile, created = Profile.objects.get_or_create(user=request.user)  
        form = ProfileForm(request.POST, request.FILES, instance=profile) 
        
        if form.is_valid():
            form.save(user=request.user)  
            return redirect("profile_list")  

    else:
        form = ProfileForm()

    return render(request, "profile.html", {"form": form})


def profile_list(request):
    profiles = Profile.objects.select_related('user').all()  # Fetch profiles with user data
    return render(request, "profile_list.html", {"profiles": profiles})
# Delete Profile
def deleteProfile(request, profile_id):
    profil = get_object_or_404(Profile, id=profile_id)
    profil.delete()
    return redirect("profile_list")


def createWork(request):
    if request.method == "POST":
        form = WorkExperienceForm(request.POST)
        if form.is_valid():
            work = form.save(commit=False)
            work.save()
            return redirect("work_list")  # Redirect to work experience list page

    else:
        form = WorkExperienceForm()

    return render(request, "work.html", {"form": form})
def work_list(request):
    work_experiences = WorkExperience.objects.all()  # Fetch all work experience data
    return render(request, "work_list.html", {"work_experiences": work_experiences})
# Delete Work Experience
def deleteWork(request, work_id):
    work = get_object_or_404(WorkExperience, id=work_id)
    work.delete()
    return redirect("work_list")


def createEducation(request):
    if request.method == "POST":
        form = EducationForm(request.POST)
        if form.is_valid():
            education = form.save(commit=False)
            education.save()
            return redirect("education_list")  # Redirect to the education list page

    else:
        form = EducationForm()

    return render(request, "education.html", {"form": form})
def education_list(request):
    educations = Education.objects.all()  # Fetch all education entries
    return render(request, "education_list.html", {"educations": educations})
# Delete Education
def deleteEducation(request, education_id):
    education = get_object_or_404(Education, id=education_id)
    education.delete()
    return redirect("education_list")


def add_certificate(request):
    if request.method == "POST":
        form = CertificateForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('certificate_list')  # Redirect after submission
    else:
        form = CertificateForm()
    return render(request, 'add_certificate.html', {'form': form})

def certificate_list(request):
    certificates = Certificate.objects.all()
    return render(request, 'certificate_list.html', {'certificates': certificates})
# Delete Certificate
def deleteCertificate(request, certificate_id):
    certificate = get_object_or_404(Certificate, id=certificate_id)
    certificate.delete()
    return redirect("certificate_list")



def createProject(request):
    if request.method == "POST":
        form = ProjectForm(request.POST, request.FILES)  # Include request.FILES for image upload
        if form.is_valid():
            project = form.save(commit=False)
            project.save()
            return redirect("project_list")  # Redirect to project list page

    else:
        form = ProjectForm()

    return render(request, "project.html", {"form": form})
def project_list(request):
    projects = Project.objects.all()  # Fetch all projects
    return render(request, "project_list.html", {"projects": projects})
# Delete Project
def deleteProject(request, project_id):
    project = get_object_or_404(Project, id=project_id)
    project.delete()
    return redirect("project_list")