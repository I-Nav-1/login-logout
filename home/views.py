from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth import logout as django_logout

# Create your views here.
def index(request):

    return render(request, 'index.html')

def deshboard(request):
    if request.user.is_anonymous:
        return redirect("/loginUser")

    return render(request, 'deshboard.html')

def loginUser(request):
    if request.method=="POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        #if user enter valid information
        user = authenticate(username=username, password=password)

        if user is not None:
            #A backend authenticated the credentials
            login( request, user)
            return redirect("/deshboard")
        else:
            # No backend authenticated the crediancials
            return render(request, 'login.html')

    return render(request, 'login.html')
def logout(request):
    django_logout(request)
    return redirect("/loginUser")
