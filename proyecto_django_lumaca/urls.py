from django.contrib import admin
from django.urls import path,include
#from proyecto_django_lumaca.views import prueba

urlpatterns = [
    path('admin/', admin.site.urls),
    path('AppCoder/', include('AppCoder.urls'))
    #path('prueba/', prueba)
]
