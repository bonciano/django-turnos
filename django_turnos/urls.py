from django.contrib import admin
from django.urls import path
from turnos import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('sobre/', views.sobre, name='sobre'),
    path('contacto/', views.contacto, name='contacto'),
    path('altausuario/', views.altausuario, name='altausuario'),
    path('altaturno/', views.altaturno, name='altaturno')
]
