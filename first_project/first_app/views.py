from django.shortcuts import render
from django.http import HttpResponse
from first_app.models import Topic,Webpage,AccessRecord
from first_app.forms import forName,userForm,userprofileForm
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse,HttpResponseRedirect
from django.contrib.auth import login,login,authenticate,logout

# Create your views here.
def index(request):
    access_list = AccessRecord.objects.order_by('date')
    webpg_dict = {'access_record':access_list}
    return render(request,'index.html',context=webpg_dict)
def redirect_to_form(request):
    form = forms.forName()
    if request.method == 'POST':
        form = forms.forName(request.POST)
        if form.is_valid():
            # do smthing
            print("Validation is successfully completed")
            print("Name "+ form.cleaned_data['name'])
            print("Email "+ form.cleaned_data['email'])
            print("Text "+ form.cleaned_data['text'])
    return render(request,'form-page.html',{'form':form})

def registration_form(request):
    registered = False
    if request.method == "POST":
        user_form = userForm(data=request.POST)
        profile_form = userprofileForm(data=request.POST)
        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            user.save()

            profile = profile_form.save(commit=False)
            profile.user = user # create one to one relationship
            if 'profile_pic' in request.FILES:
                profile.profile_pic = request.FILES['profile_pic']
            profile.save()
            registered = True
        else:
            print(user_form.errors,profile_form.errors)
    else:
        user_form = userForm()
        profile_form = userprofileForm()
    return render(request,"register.html",{'user_form':user_form,
    'profile_form':profile_form,
    'registered':registered})

def user_login(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username,password=password)
        if user:
            if user.is_active:
                login(request,user)
                return HttpResponseRedirect(reverse('index'))
            else:
                return HttpResponse("Account not active!")
        else:
            print("Someone tried to login and failed")
            print("username: {} and password {}".format(username,password))
            return HttpResponse("Invalid Login detail supplied!")
    else:
        return render(request,'login.html',{})

@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('index'))
    
@login_required
def special(request):
    return HttpResponse("you are logged in, Nice")

