from django import views
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),

    path('blog/', views.blog, name='blog'),
    path('single-blog/<pk>/',views.singleBlog, name='single-blog'),

    path('add-blog/', views.addBlog, name='add-blog'),

    path('gallery', views.gallery, name='gallery'),

    path('contact/', views.contact, name='contact'),
    path('get-involved/', views.getInvolved, name='get-involved'),
    path('login/', views.login, name='login'),

    path('volunteers/', views.volunteering, name='volunteers'),
    path('members/', views.becomeMember, name="members"),
    path('primary-health-care/', views.primaryHealCare, name="primary-health-care"),
    path('peace-education/', views.peaceEducation, name="peace-education"),
    path('art/', views.art, name="art"),

    path('application-complete', views.applicationComplete, name='application-complete' ),
    path('thank-you/', views.thankYou, name='thank-you'),
]