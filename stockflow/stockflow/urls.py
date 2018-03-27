
from django.conf.urls import url, include
from django.contrib import admin
from stockflow import views

urlpatterns = [
    url(r'^$', views.login_redirect, name='login_redirect'),
    url(r'^admin/', admin.site.urls),
    url(r'^account/', include('accounts.urls', namespace='accounts')),
    url(r'^account/', include('django.contrib.auth.urls')),
    url(r'^home/', include('home.urls', namespace='home')),
    url(r'^api/', include('api.urls')),
    
]
