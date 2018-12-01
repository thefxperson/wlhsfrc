from django.conf.urls import url
from . import views

urlpatterns = [
	url("^$", views.index, name="index"),
	url('^about/$', views.about, name='about'),
    url('^about-first/$', views.aboutfirst, name='aboutfirst'),
    url('^about-our-robots/$', views.aboutrobot, name='aboutrobot'),
    url('^outreach/$', views.outreach, name='outreach'),
    url('^contact/$', views.contact, name='contact'),
]