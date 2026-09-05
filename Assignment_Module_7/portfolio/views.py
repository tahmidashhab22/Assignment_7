from django.shortcuts import render, get_object_or_404
from .models import Project


# Homepage view - just renders a template, no database needed here.
def home(request):
    return render(request, 'portfolio/home.html')


# About page view - also static content.
def about(request):
    return render(request, 'portfolio/about.html')


# Projects page view - fetches ALL projects from the database
# and sends them to the template so they can be listed.
def projects(request):
    all_projects = Project.objects.all()
    context = {
        'projects': all_projects
    }
    return render(request, 'portfolio/projects.html', context)


# Project details view - fetches ONE project by its id (pk).
# If the project doesn't exist, this automatically shows a 404 page.
def project_detail(request, pk):
    project = get_object_or_404(Project, pk=pk)
    context = {
        'project': project
    }
    return render(request, 'portfolio/project_detail.html', context)
