"""guestmapp URL Configuration

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
from django.conf.urls import url, include
from django.contrib import admin
from order import views as order_views
from account import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^ajax_login/$', views.ajax_login, name = "ajax_login"),
    url(r'^ajax_register/$', views.ajax_register, name = "ajax_register"),
    url(r'^ajax_logout/$', views.ajax_logout, name="ajax_logout"),
    url(r'^ajax_order/$', order_views.ajax_order, name="ajax_order"),
    url(r'^$', views.home, name = "home"),
    url(r'^planprices/$', views.planprices, name = "planprices"),
    url(r'^ownguestmapp/$', views.ownguestmapp, name="ownguestmapp"),
    url(r'^guestmapp/$', views.guestmapp, name = "guestmapp"),
    url(r'^newpassword/$', views.newpassword),
]
