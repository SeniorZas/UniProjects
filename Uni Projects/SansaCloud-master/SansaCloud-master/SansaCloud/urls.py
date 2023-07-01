"""SansaCloud URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from SansaCloud.views import *
from Foro.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('registro.html', register),
    path('login.html', custom_login),
    path('logout.html', custom_logout),
    path('test.html', test),
    path('foro.html',foro,name='foro'),
    path('addInForum.html',addInForum,name='addInForum'),
    path('addInDiscussion.html',addInDiscussion,name='addInDiscussion'),
    path('home.html', home, name="homepage"),
    path('carreras.html', carreras),
    path('ramos.html', ramos),
    path('mat021.html', mat021),
    path('iwi131.html', iwi131),
    path('IngenieriaCivilInformatica.html', ingCivilInf),
    path('mat021.html', mat021),
    path('Notas Semestrales.pdf', notasSemestrales),
    path('Certamen1-2014-1.pdf', c120141),
    path('Certamen1-2014-2.pdf', c120142),
    path('Certamen1-2015-1.pdf', c120151),
    path('Certamen2-2015-2.pdf', c220152),
    path('Certamen3-2014-2.pdf', c320142),
    path('CertamenGlobalMat021.pdf', cgmat021),
    path('Control1-2015-1.pdf', co120151),
    path('Ejercicios de Inducción.pdf', ejerciciosInduccion),
    path('Guía de Sumatorias y Progresiones.pdf', guiaSumyPro),
    path('PautaTallerC2-1.pdf', pautaTallerC2),
    path('Taller 1 Dasarrollado.pdf', Taller1Mat021),
    path('Taller 2 Desarrollado.pdf', Taller2Mat021),
    path('hrw130.html', hrw130),
    path('fis100.html', fis100),
    path('Resumen.pdf', ResumenHrw130),
    path('Taller 1 Hrw130.pdf', Taller1Etica),
    path('UVA1.pdf', UVA1),
    path('UVA9.pdf', UVA9),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)