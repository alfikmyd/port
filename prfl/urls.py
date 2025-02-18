from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from .import views
from .views import add_certificate, certificate_list,createProfile, profile_list,createEducation, education_list
from .views import createProject, project_list,createWork, work_list
from .views import deleteProfile, deleteWork,deleteEducation,deleteCertificate,deleteProject

urlpatterns = [
    path('',createProfile, name='createProfile'),
    path("profile-list/", profile_list, name="profile_list"),
    # path('profile/', profile_list, name='profile'), 
    path("profiles/delete/<int:profile_id>/", deleteProfile, name="delete_profile"),
   
    path("create-education/", createEducation, name="create_education"),
    path("education-list/", education_list, name="education_list"),   
    path("education/delete/<int:education_id>/", deleteEducation, name="delete_education"),

    path('add-certificate/', add_certificate, name='add_certificate'),
    path('certificate-list/', certificate_list, name='certificate_list'),
    path("certificates/delete/<int:certificate_id>/", deleteCertificate, name="delete_certificate"),

    path("create-project/", createProject, name="create_project"),
    path("project-list/", project_list, name="project_list"),
    path("projects/delete/<int:project_id>/", deleteProject, name="delete_project"),

    path("create-work/", createWork, name="create_work"),
    path("work-list/", work_list, name="work_list"),
    path("work/delete/<int:work_id>/", deleteWork, name="delete_work"),

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
