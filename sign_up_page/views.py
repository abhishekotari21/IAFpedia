from django.shortcuts import render

# Create your views here.
def signup(request):
    return render(request,'signup_page.html')
def login(request):
    return render(request,'login_page.html')
def forg_pass(request):
    return render(request,'forg_pass_page.html')