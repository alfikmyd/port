from django.contrib import admin
from .models import Profile, Education,Certificate,WorkExperience,Project

admin.site.register(WorkExperience)
admin.site.register(Profile)
admin.site.register(Education)
admin.site.register(Certificate)
admin.site.register(Project)

