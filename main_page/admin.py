from django.contrib import admin

from .models import BlogPost, HistoricalEvent
# Register your models here.
admin.site.register(BlogPost)
admin.site.register(HistoricalEvent)