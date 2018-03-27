from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$',views.home, name='home'),
    url(r'^newwallet/$',views.newwallet, name='newwallet'),
    url(r'^wallet/(?P<name>[\w.@+\s]+)/$',views.wallet, name='wallet'),
    url(r'^wallet/(?P<name>[\w.@+\s]+)/edit$',views.editwallet, name='editwallet'),
    url(r'^deletewallet/(?P<name>[\w.@+\s]+)/$',views.deletewallet, name='deletewallet'),
    url(r'^company/(?P<symbol>\w+)/$',views.company, name='company'),
    url(r'^allcompanies/$',views.allcompanies, name='allcompanies'),
]
