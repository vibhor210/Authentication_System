from django.shortcuts import redirect, render
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages

def index(request):
    if request.user.is_authenticated:
        return redirect("landing")
    if request.method=="POST":
        # Get the post parameters
        username=request.POST['username']
        password=request.POST['password']
        user=authenticate(username= username, password= password)
        if user is not None:
            login(request, user)
            messages.success(request, "Successfully Login")
            return redirect("landing")
        else:
            messages.warning(request, "Invalid Credential")
            return redirect("/")

    return render(request, "index.html")

def register(request):
    if request.user.is_authenticated:
        return redirect("landing")
    if request.method == "POST":
        username = request.POST['username']
        email = request.POST['email']
        pass1 = request.POST['password1']
        pass2 = request.POST['password2']
        print(username.isalnum())
        if len(username)<8:
            messages.warning(request, "Username alteast contain 8 charater")
            return redirect("register")
        if (not username.isalnum()) or (username.isnumeric()):
            messages.warning(request, "Username should contain only letter and number")
            return redirect("register")
        if (username[0].isnumeric()) :
            messages.warning(request, "Username should start form a alphabet")
            return redirect("register")
        if pass1 != pass2:
            messages.warning(request, "Password not matches")
            return redirect("register")

        user = User.objects.create_user(username, email, pass1)
        user.save()
        messages.success(request, "Successfully registered")
        return redirect("/")
    return render(request, "register.html")

@login_required(login_url="/")
def landing(request):
    return render(request, "landing.html")

def log_out(request):
    logout(request)
    messages.success(request,"Successfully Logout")
    return redirect("index")