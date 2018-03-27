from django.conf.urls import url
from home.views import WalletListView, WalletView

helper_patterns = [
    url(r'^home/$', WalletListView.as_view(), name='apihome'),
    url(r'^home/(?P<pk>[0-9]+)/$', WalletView.as_view(), name='get_apihome'),
]

urlpatterns = helper_patterns
