from django.urls import path
from . import views

urlpatterns = [
    path('',views.home,name='main_page'),
    path('about_us/',views.about_us,name='about_us'),
    path('sources/',views.sources,name='sources'),
    path('privacy_policy/',views.privacy_policy,name='privacy_policy'),
    path('contactus/',views.contactus,name='contactus'),
    path('newsfeed/',views.newsfeed,name='newsfeed'),
    path('exams/',views.exams,name='exams'),
    path('exam_subpage/',views.exam_subpage,name='exam_subpage'),
    path('hof_army/',views.hof_army,name='hof_army'),
    path('hof_navy/',views.hof_navy,name='hof_navy'),
    path('hof_airforce/',views.hof_airforce,name='hof_airforce'),
    path('donations/',views.donations,name='donations'),
    path('settings/',views.settings,name='settings'),
]
