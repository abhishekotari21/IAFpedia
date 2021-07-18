from django.contrib import admin

from .models import BlogPost, HistoricalEvent, ArmyExam, NavyExam, AirforceExam
# Register your models here.
admin.site.register(BlogPost)
admin.site.register(HistoricalEvent)

class ExamAdmin(admin.ModelAdmin):
    readonly_fields = ('id',)
admin.site.register(ArmyExam, ExamAdmin)
admin.site.register(NavyExam, ExamAdmin)
admin.site.register(AirforceExam, ExamAdmin)