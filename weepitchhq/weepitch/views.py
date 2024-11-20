from django.shortcuts import render
from .models import Weepitch
from .forms import WeepitchForm, UserRegistrationForm
from django.shortcuts import get_object_or_404 , redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login
# Create your views here.
def index(request):
    return render(request, "index.html")



def weepitch_list(request):
    weepitchs = Weepitch.objects.all().order_by('-created_at')
    return render(request, "weepitch_list.html", {'weepitchs': weepitchs})
@login_required
def weepitch_create(request):
    if request.method == 'POST': 
       form  = WeepitchForm(request.POST, request.FILES)
       if form.is_valid():
           weepitch = form.save(commit=False)
           weepitch.user = request.user
           weepitch.save()
           return redirect('weepitch_list')
    else:
        form = WeepitchForm()
    return render(request, "weepitch_form.html", {'form': form})
@login_required
def weepitch_edit(request , weepitch_id):
    weepitch = get_object_or_404(Weepitch, pk=weepitch_id , user = request.user)
    if request.method == 'POST':
        form = WeepitchForm(request.POST, request.FILES, instance=weepitch)
        if form.is_valid():
            weepitch = form.save(commit=False)
            weepitch.user = request.user
            weepitch.save()
            return redirect('weepitch_list')
        
    else:
        form = WeepitchForm(instance=weepitch)
    return render(request, "weepitch_form.html", {'form': form})
@login_required
def weepitch_delete(request , weepitch_id):
    weepitch = get_object_or_404(Weepitch, pk=weepitch_id , user = request.user)
    if request.method == 'POST':
        weepitch.delete()
        return redirect('weepitch_list')
    return render(request, "weepitch_confirm_delete.html", {'weepitch': weepitch})


def register(request):
       if request.method == 'POST':
           form = UserRegistrationForm(request.POST)
           if form.is_valid():
               user = form.save(commit=False)
               user.set_password(form.cleaned_data['password1'])
               user.save()
               login(request, user)
               return redirect('weepitch_list')
       else:
           form = UserRegistrationForm()
       return render(request, "registration/register.html", {'form': form})
    