from django.contrib import admin
from .models import *
# Register your models here.

@admin.register(ContactFormMessage)
class ContactFormMessageAdmin(admin.ModelAdmin):
    list_display = ("first_name", "last_name", "email", "phone_number", "date_sent")

@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    list_display = ("blog_title", "date_added")

@admin.register(GettingInvolvedLead)
class GettingInvolvedLeadAdmin(admin.ModelAdmin):
    list_display = ("first_name", "last_name", "email", "phone_number", "application_date")

@admin.register(OfficialDocument)
class OfficialDocumentsAdmin(admin.ModelAdmin):
    list_display = ("title", "category")

@admin.register(Volunteer)
class VolunteerAdmin(admin.ModelAdmin):
    list_display = ("first_name", "last_name", 'email', 'phone_number', 'nationality', 'membership_status')
