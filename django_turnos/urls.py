from django.contrib import admin
from django.urls import path
from turnos import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('signup/', views.signup, name='signup'),
    path('signin/', views.signin, name='signin'),
    path('signout/', views.signout, name='signout'),
    path('sobre/', views.sobre, name='sobre'),
    path('contacto/', views.contacto, name='contacto'),
    path('altaturno/', views.altaturno, name='altaturno')
]
