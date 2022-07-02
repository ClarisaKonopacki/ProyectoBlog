"""ProyectoWeb URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from ProyectoApp import views
from django.conf import settings
from django.conf.urls.static import static


#Cambios en ruta!!

from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import handler404
from ProyectoApp.views import Error404View, Error403View, Error500View


urlpatterns = [
    path("", views.index, name="index"),
    path('blog/', include('ProyectoApp.urls')),
    path('CuentaBlog/', include('CuentaBlog.urls')),
    path('admin/', admin.site.urls),
   ]

handler404 = Error404View.as_view()
handler403 = Error403View.as_view()
handler500 = Error500View.as_view()

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)