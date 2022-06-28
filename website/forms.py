from dataclasses import field
from email.policy import default
from pyexpat import model
from django.forms import ModelForm, TextInput, ImageField, Textarea, EmailInput, Select, FileInput
from ckeditor.fields import RichTextFormField
from ckeditor_uploader.fields import RichTextUploadingFormField
from .models import *

class AddBlogFrom(ModelForm):
    class Meta:
        model = Blog
        fields = ['title', 'featured_image', 'content']
        widgets = {
            'title': TextInput(attrs={'class':'form-control', 'placeholder':'Blog title'}),
            'content': RichTextUploadingFormField(config_name=default)
        }


class ContactFormMessageForm (ModelForm):
    class Meta:
        model = ContactFormMessage
        fields = ['first_name', 'last_name', 'email', 'phone_number', 'client_message' ]
        widgets = {
            'first_name': TextInput(attrs={'class':'form-control', 'placeholder': 'Your first name'}),
            'last_name': TextInput(attrs={'class':'form-control', 'placeholder': 'Your last name'}),
            'email': EmailInput(attrs={'class':'form-control', 'placeholder': 'Your email address'}),
            'phone_number': TextInput(attrs={'class':'form-control', 'placeholder': 'Your phone number'}),
            'client_message': Textarea(attrs={'class':'form-control', 'placeholder': 'Type your message here', 'rows': '5'}),
        }

class GettingInvolvedLeadForm(ModelForm):
    class Meta:
        model = GettingInvolvedLead
        fields = ['first_name', 'last_name', 'email', 'phone_number',
        'category', 'education', 'experience', 'college', 'expectations', 'cv' 
        ]

        widgets = {
            'first_name': TextInput(attrs={'class':'form-control', 'placeholder': 'Your first name'}),
            'last_name': TextInput(attrs={'class':'form-control', 'placeholder': 'Your last name'}),
            'email': EmailInput(attrs={'class':'form-control', 'placeholder': 'Your email address'}),
            'phone_number': TextInput(attrs={'class':'form-control', 'placeholder': 'Your phone number'}),
            'category': Select(attrs={'class': 'form-control'}),
            'experience': Textarea(attrs={'class':'form-control', 'placeholder': 'Type your experience here', 'rows': '3'}),
            'education': TextInput(attrs={'class':'form-control', 'placeholder': 'Your hiest degree'}),
            'college': TextInput(attrs={'class':'form-control', 'placeholder': 'Your college or school'}),
            'expectations': Textarea(attrs={'class':'form-control', 'placeholder': 'Type your expectations here', 'rows': '3'}),
            'cv': FileInput(attrs={'class': 'form-control'}),


        }


class VolunteersForm(ModelForm):
    class Meta:
        model = Volunteer
        fields = ['first_name', 'last_name', 'email', 'phone_number', 'nationality',
        'current_adress', 'level_of_education', 'specialization', 'graduation_country',
        'experience', 'consept_note', 'owns_a_computer', 'cv']
        widgets = {
            'first_name': TextInput(attrs={'class':'form-control', 'placeholder': 'Your first name'}),
            'last_name': TextInput(attrs={'class':'form-control', 'placeholder': 'Your last name'}),
            'email': TextInput(attrs={'class':'form-control', 'placeholder': 'email'}),
            'phone_number': TextInput(attrs={'class':'form-control', 'placeholder': 'Your phone number'}),
            'nationality': TextInput(attrs={'class':'form-control', 'placeholder': 'nationality'}),
            'current_adress': TextInput(attrs={'class':'form-control', 'placeholder': 'current adress'}),
            'level_of_education': TextInput(attrs={'class':'form-control', 'placeholder': 'level of education'}),
            'specialization': TextInput(attrs={'class':'form-control', 'placeholder': 'specialization'}),
            'graduation_country': TextInput(attrs={'class':'form-control', 'placeholder': 'graduation country'}),
            'experience': Textarea(attrs={'class':'form-control', 'placeholder': 'Your Experience'}),
            'consept_note': Textarea(attrs={'class':'form-control', 'placeholder': 'Your Consept'}),
            'owns_a_computer': TextInput(attrs={'class':'form-control', 'placeholder': 'Yes or No'}),
            'cv': FileInput(attrs={'class':'form-control', 'placeholder': 'Yes or No'}),
        }