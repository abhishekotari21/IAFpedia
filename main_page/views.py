from django.shortcuts import render, redirect
from .models import BlogPost, HistoricalEvent, ArmyExam, NavyExam, AirforceExam
from sign_up_page.models import Account

from django.contrib.auth.models import User,auth
from django.contrib import messages

# Create your views here.
def home(request):
    return render(request,'main_page.html')

def about_us(request):
    return render(request,'about_us.html')

def sources(request):
    return render(request,'sources.html')

def privacy_policy(request):
    return render(request,'privacy_policy_page.html')

def contactus(request):
    return render(request,'contact_us.html')

def newsfeed(request):
    BlogPosts=BlogPost.objects.all()
    context={
        'BlogPosts':BlogPosts,
    }
    return render(request,'newsfeed.html',context)

def exams(request):
    ArmyExams=ArmyExam.objects.all()
    context={
        'ArmyExams':ArmyExams,
    }
    return render(request,'exam_main_page.html',context)

def exams_army(request):
    ArmyExams=ArmyExam.objects.all()
    context={
        'ArmyExams':ArmyExams,
    }
    return render(request,'exam_main_page.html',context)

def exams_navy(request):
    NavyExams=NavyExam.objects.all()
    context={
        'NavyExams':NavyExams,
    }
    return render(request,'exam_navy_main_page.html',context)

def exams_airforce(request):
    AirforceExams=AirforceExam.objects.all()
    context={
        'AirforceExams':AirforceExams,
    }
    return render(request,'exam_airforce_main_page.html',context)

def exam_subpage(request):
    return render(request,'exam_subpage.html')

def hof_army(request):
    return render(request,'hof_army.html')

def hof_navy(request):
    return render(request,'hof_navy.html')

def hof_airforce(request):
    return render(request,'hof_airforce.html')

def he(request):
    HisEvents=HistoricalEvent.objects.all()
    context={
        'HisEvents':HisEvents,
    }
    return render(request,'he.html',context)

def donations(request):
    return render(request,'donation_page.html')

def settings(request):
    return render(request,'settings.html')

def settings_edit(request):
    if request.method == 'POST':
        userid=request.user.id
        Account.objects.get(pk=userid).delete()
        fullname=request.POST['fname_test']
        username=request.POST['uname_test']
        dob=request.POST['date_test']
        gender=request.POST['btn']
        email=request.POST['email_test']
        state=request.POST['state']
        city=request.POST['city']
        pincode=request.POST['pincode_test']
        password1=request.POST['pass_test1']
        password2=request.POST['pass_test2']
        if password1==password2:
            if Account.objects.filter(email=email).exists() and email!='':
                messages.info(request, 'Email already used. Use another email id.')
                return redirect('settings_edit')
            elif Account.objects.filter(username=username).exists():
                messages.info(request, 'Username not available. Use another username')
                return redirect('settings_edit')
            else:
                user=Account.objects.create_user(fullname=fullname,username=username, dob=dob, gender=gender, email=email, state=state,city=city, pincode=pincode, password=password1)
                user.save()
                messages.info(request, 'Account details updated.')
                user = auth.authenticate(username=username,password=password1)
                auth.login(request,user)

                return redirect('settings')
        else:
            messages.info(request, 'Make sure your passwords match.')
            return redirect('settins_edit')
    else:
        return render(request,'settings_edit_account.html')