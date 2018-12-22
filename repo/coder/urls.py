from django.conf.urls import url
from . import views

app_name = 'coder'

urlpatterns = [
	
	url(r'^$', views.index, name='index'),
	url(r'^(?P<album_id>[0-9]+)/$', views.detail, name='detail'),
	url(r'^post/(?P<news_id>[0-9]+)/$', views.story, name='story'),
	url(r'^about/$', views.about, name='about'),
	url(r'^contact/$', views.contact, name='contact'),
	url(r'^team/$', views.team, name='team'),

]