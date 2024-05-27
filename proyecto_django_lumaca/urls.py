from django.contrib import admin
from django.urls import path,include
from AppCoder.views import estudianteForm
#from proyecto_django_lumaca.views import prueba

urlpatterns = [
    path('admin/', admin.site.urls),
    path('AppCoder/', include('AppCoder.urls')),
    path('estudiantes/', estudianteForm)
    #path('prueba/', prueba)
]
