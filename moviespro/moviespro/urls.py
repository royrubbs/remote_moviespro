"""moviespro URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Import the include() function: from django.conf.urls import url, include
    3. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import url
from django.contrib import admin
from moviesapp import views
from django.views.generic import TemplateView
urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$',views.homeview),
    url(r'^telugu/',views.teluguview,name='moviesapp1'),
    url(r'^hindi/',views.hindiview),
    url(r'^english/',views.englishview),
    url('^booknow/',TemplateView.as_view(template_name='booknowview.html'),name='moviesapp2'),
    url('^telugudata/',TemplateView.as_view(template_name='telugudata.html'),name='moviesapp')

]
