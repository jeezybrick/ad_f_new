"""Fits URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url
from django.contrib import admin
from django.conf.urls.static import static
from django.conf import settings
from init import views

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),

    url(r"^$", views.HomeView.as_view(), name='home'),

    url(r"^thanks/$", views.ThanksView.as_view(), name='thanks'),

    url(r"^policy/$", views.PolicyView.as_view(), name='policy'),

    url(r"^terms/$", views.TermsView.as_view(), name='terms'),

    url(r"^faq/$", views.FaqView.as_view(), name='faq'),

    url(r"^join-network/$", views.JoinNetworkView.as_view(), name='join-network'),

    url(r"^publisher/advertisers/$", views.AdvertisersView.as_view(), name='advertisers'),

    url(r"^publisher/sites/get-code/$", views.GetCodeView.as_view(), name='get-code'),


]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
