from django.conf.urls import include
from django.contrib import admin
from django.urls import path


urlpatterns = [
    path('admin/', admin.site.urls),
   
    # REST FRAMEWORK URLS
     path('api/servico/', include('servicos.urls')),
     path('api/cadastro/', include('conta.api.urls')),
     
]
