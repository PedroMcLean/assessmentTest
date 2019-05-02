from django.shortcuts import render
from .models import Client
from django.contrib.auth.decorators import login_required

#Enforcing that the user is logged in before navigation can occur, and displaying all data in the DB.
@login_required(login_url="/accounts/login/")
def clients(request):
    clients = Client.objects.all().order_by('clientName')
    return render(request, 'clients/client_list.html', {'clients':clients})
