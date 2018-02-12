"""Skills URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url,include
from django.contrib import admin
from . import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),

    url(r'^$', views.Homepage.as_view(), name='home'),
    #/contact
    url(r'^contact/$',views.Contact_team.as_view(), name='contact_team'),

    #/accounts/login
    url(r'^accounts/', include('accounts.urls', namespace='accounts')),
    #accounts/logout
    url(r'^accounts/', include('django.contrib.auth.urls')),
    url(r'^test/$', views.Test.as_view(), name='test'),
    url(r'^thanks/$', views.Thanks.as_view(), name='thanks')
]
