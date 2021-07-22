from django.contrib import admin

# Register your models here.
from .models import Interviews , Job , Questions
from django.contrib.auth.models import User

@admin.register(Job)
class JobAdmin(admin.ModelAdmin):
    list_display = ["name","description","created_by",'created_at']
    list_filter = ["created_at"]
    # list_editable = ["name","description"]

@admin.register(Questions)
class QuestionAdmin(admin.ModelAdmin):
    list_display = ["question","answer","questDur"]
    # list_editable = ["Title"]
    # prepopulated_fields = {""}

@admin.register(Interviews)
class InterviewAdmin(admin.ModelAdmin):
    list_display = ["title","job","created_by"]
    list_filter = ["created_at"]
    # list_editable = ["Title"]
    # prepopulated_fields = {""}

