from django.contrib import admin
from .models import Project


# Registering the Project model so it shows up in the Django Admin.
# I'm also customizing how it looks in the admin list page.
@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('title', 'tech_used', 'created_at')
    search_fields = ('title', 'tech_used')
