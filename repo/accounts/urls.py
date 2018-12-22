from django.conf.urls import url
from accounts import views
from django.contrib.auth import views as auth_views

app_name = 'accounts'

urlpatterns = [

    url(r'^signup/', views.signup, name='signup'),
    url(r'^login/', auth_views.login, name='login'),
    url(r'^logout/', auth_views.logout, name='logout'),



]
