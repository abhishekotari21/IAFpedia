from django.shortcuts import render
from .models import BlogPost, HistoricalEvent, ArmyExam, NavyExam, AirforceExam
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