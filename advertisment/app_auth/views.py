from django.shortcuts import redirect, render

# from .forms import AdvertismentForm
from django.urls import reverse, reverse_lazy
from django.contrib.auth.decorators  import login_required
from django.contrib.auth import  authenticate,logout,login as login_dj
from .forms import ExtendedUserCreationForm

# Create your views here.



def login(request):
    redirect_url= reverse('profile')
    if request.method == "GET":
        if request.user.is_authenticated:
            return redirect(redirect_url)
        else:
            return render(request,'app_auth/login.html')
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request,username = username, password = password)
        if user is not None:
            login_dj(request,user)
            return redirect(redirect_url)
    return render(request,'app_auth/login.html',context={'error':"В форме возникла ошибка"})




@login_required(login_url= reverse_lazy('login'))
def profile(request):
    return render(request,'app_auth/profile.html')

def register(request):
    if request.method == "POST":
        form = ExtendedUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            user = authenticate(username=request.POST['username'], password=request.POST['password1'])
            login_dj(request, user=user)
            return redirect('profile')
    else:
        form = ExtendedUserCreationForm()
    context = {"form":form}
    return render(request,'app_auth/register.html',context= context)

def logout_vi(request):
    logout(request)
    return redirect(reverse('login'))
