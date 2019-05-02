from django.shortcuts import render
from .models import Project
from django.contrib.auth.decorators import login_required

#Enforcing that the user is logged in before navigation can occur, and displaying all data in the DB.
@login_required(login_url="/accounts/login/")
def projects(request):
    projects = Project.objects.all().order_by('projectName')
    return render(request, 'projects/project_list.html', {'projects':projects})
