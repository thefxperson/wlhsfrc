from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('about-first/', views.aboutfirst, name='aboutfirst'),
    path('about-our-robots/', views.aboutrobot, name='aboutrobot'),
    path('outreach/', views.outreach, name='outreach'),
    path('contact/', views.contact, name='contact'),
]
